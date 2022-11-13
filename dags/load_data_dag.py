from airflow import DAG
from datetime import datetime, timedelta
# from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))
from database.populatedb import csv_to_sql

default_args = {
    'owner': 'emtinan',
    'retries': 2,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id ='first_dagD1',
    default_args= default_args,
    description = "our first dag",
    start_date = datetime(2022,10,4,10),
    schedule_interval = '@daily'
) as dag:
#A task bash operator = runs bash command, python operator = runs python code
    task1 = PythonOperator(
        task_id = 'load_vehicle_data',
        python_callable = populate_trajectory_table
    )
    task1

# how to share data between multiple tasks: output of one task -> input of another task
# python operators, python functions parameter of one task comes from output of another task
# output of tasks is recorded (where?)
# airflow done scom push , scom pull