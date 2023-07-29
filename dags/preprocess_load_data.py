from airflow.decorators import dag, task
from datetime import datetime
import pandas as pd
from pathlib import Path
import sys
import config

python_path = config.python_path
dir = config.dir

sys.path.append(str(Path(__file__).parent.parent))
from scripts.read_data import Reader
from database.populatedb import Database

@dag(
    schedule= None,
    start_date= datetime(2023,7,20,1),
    catchup= False,
)
def preprocess_load_data():
    """
    A pipeline that:
      - reads raw data from csv file, 
      - preprocess the data, spliting it into 2 dataframes
      - load the data into 2 tables in the database
    """
    
    @task.external_python(python=python_path)
    def preprocess_data(data_file:str) -> dict[str, pd.DataFrame]:
    # def preprocess(data_file:str = "data/20181024_d1_0830_0900.csv"):
        reader = Reader()
        vehicles, trajectories = reader.data_dfs(data_file)

        return {"vehicles": vehicles, "trajectories":trajectories}

    @task.external_python(python=python_path)
    def load_vehicles(df:pd.DataFrame):  
        db = Database()
        db.vehicle_dataframe_to_sql(df)

    @task.external_python(python=python_path)
    def load_traj(df:pd.DataFrame):
        db = Database()
        db.trajectory_dataframe_to_sql(df)
   

    data_file = dir + "/data/20181024_d1_0830_0900.csv"
    dfs = preprocess_data(data_file)
    load_vehicles(dfs["vehicles"])
    load_traj(dfs["trajectories"])

preprocess_load_data()