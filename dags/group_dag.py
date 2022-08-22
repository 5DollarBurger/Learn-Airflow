from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.subdag import SubDagOperator
from airflow.utils.task_group import TaskGroup

from groups.groups_transforms import taskgroup_transforms
from subdags.subdags_downloads import subdag_downloads

with DAG(
    dag_id='group_dag', 
    start_date=datetime(2022, 1, 1), 
    schedule_interval='@daily', 
    catchup=False
    ) as dag:

    args = {
        'start_date': dag.start_date,
        'schedule_interval': dag.schedule_interval,
        'catchup': dag.catchup
    }
    
    group_dag_id = 'downloads'
    downloads = SubDagOperator(
        task_id=group_dag_id,
        subdag=subdag_downloads(
            parent_dag_id=dag.dag_id,
            child_dag_id=group_dag_id,
            args=args
            )
    )
 
    check_files = BashOperator(
        task_id='check_files',
        bash_command='sleep 10'
    )

    group_id = 'transforms'
    transforms = taskgroup_transforms(
        group_id=group_id
        )
 
    downloads >> check_files >> transforms
