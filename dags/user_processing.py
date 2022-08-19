from datetime import datetime

from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

with DAG(
    dag_id='user_processing', 
    start_date=datetime(year=2022, month=1, day=1), 
    schedule_interval='@daily', 
    catchup=False
    ) as dag:
    
    create_table = PostgresOperator()
