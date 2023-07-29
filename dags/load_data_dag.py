from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from pathlib import Path
import sys
import config

dir = config.dir
env_path = config.env_path
python_path = config.python_path


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['emtinan.s.e.osman@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

with DAG(
    dag_id ='load_data_dag',
    default_args= default_args,
    description = "Dag to load data from csv files to database",
    start_date = datetime(2023,7,22,2),
    schedule_interval = None,
    # schedule_interval = timedelta(minutes=10),
    catchup = False,
) as dag:
    run_dbt = BashOperator(
        task_id= "load_data_into_db",
        bash_command= f"source {env_path}/bin/activate && cd {dir}/database && python3 populatedb.py &> load.log ",
        # env= dict(PATH=python_path),
    )