# Airflow is an optional dependency and is not required for the local SLA evaluator.
from datetime import datetime
try:
    from airflow import DAG
    from airflow.operators.empty import EmptyOperator
    with DAG('claims_daily',start_date=datetime(2026,1,1),schedule='@daily',catchup=False) as dag:
        completed=EmptyOperator(task_id='completed')
except ImportError:
    dag=None
