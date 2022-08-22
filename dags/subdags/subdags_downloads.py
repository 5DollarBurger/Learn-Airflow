from airflow import DAG
from airflow.operators.bash import BashOperator


def subdag_downloads(parent_dag_id: str, child_dag_id: str, args) -> DAG:
    
    with DAG(
        dag_id=f"{parent_dag_id}.{child_dag_id}", 
        start_date=args['start_date'],
        schedule_interval=args['schedule_interval'],
        catchup=args['catchup']
        ) as dag:

        download_a = BashOperator(
        task_id='download_a',
        bash_command='sleep 1'
        )

        download_b = BashOperator(
            task_id='download_b',
            bash_command='sleep 2'
        )
    
        download_c = BashOperator(
            task_id='download_c',
            bash_command='sleep 3'
        )

        return dag
