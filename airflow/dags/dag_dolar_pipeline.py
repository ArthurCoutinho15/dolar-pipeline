import os
import sys

sys.path.append('/opt/airflow/external_scripts')  


from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def run_pipeline():
    import sys
    sys.path.append('/opt/airflow/external_scripts')
    from main import main
    main()

with DAG(
    dag_id='dolar_pipeline_dag',
    default_args=default_args,
    description='Pipeline ETL de cotação do dólar rodando 3 vezes ao dia',
    schedule_interval='0 10,15,20 * * *',  
    start_date=datetime(2024, 6, 1),
    catchup=False,
    tags=['dolar', 'etl'],
) as dag:

    run_pipeline = PythonOperator(
        task_id='executa_pipeline_dolar',
        python_callable=run_pipeline,
    )

    run_pipeline
