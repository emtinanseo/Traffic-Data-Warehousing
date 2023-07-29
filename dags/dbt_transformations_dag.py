from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
from datetime import timedelta
import config

dir = config.dir
env_path = config.env_path
dbt_path = config.dbt_path
dbt_project_dir = config.dbt_project_dir
dbt_profile_dir = config.dbt_profile_dir

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
    dag_id ='dbt_transformations',
    default_args= default_args,
    description = "Dag to run dbt transformation",
    start_date = datetime(2023,7,22,2),
    schedule_interval = None,
    # schedule_interval = timedelta(minutes=10),
    catchup = False,
) as dag:
    
    run_dbt = BashOperator(
        task_id = "run_dbt",
        bash_command = f'''
        cd {dir} &&\
             source {env_path}/bin/activate &&\
                 dbt run --project-dir {dbt_project_dir} --profiles-dir {dbt_profile_dir} &> logs/dbt_run.log
                 ''',
    )
    

    test_dbt = BashOperator(
        task_id= "test_dbt",
        bash_command = f'''
        cd {dir} &&\
             source {env_path}/bin/activate &&\
                 dbt test --project-dir {dbt_project_dir} --profiles-dir {dbt_profile_dir} --store-failures &> logs/dbt_test.log
                 ''',
    )

    gen_docs_dbt = BashOperator(
        task_id= "gen_docs_dbt",
        bash_command = f'''
        cd {dir} &&\
             source {env_path}/bin/activate &&\
                 dbt docs generate --project-dir {dbt_project_dir} --profiles-dir {dbt_profile_dir} &> logs/dbt_docs.log
                 ''',
    )

    run_dbt >> test_dbt >> gen_docs_dbt

