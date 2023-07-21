from airflow.decorators import dag, task
from datetime import datetime
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))
from scripts.read_data import Reader
from database.populatedb import Database

@dag(
    schedule= None,
    start_date= datetime(2023,7,20,20),
    catchup= False,
)
def preprocess_load_data():
    """
    A pipeline that:
      - reads raw data from csv file, 
      - preprocess the data, spliting it into 2 dataframes
      - load the data into 2 tables in the database
    """
    
    @task(multiple_outputs=True)
    def preprocess_data(data_file:str = "data/20181024_d1_0830_0900.csv"):
        reader = Reader()
        vehicles, trajectories = reader.data_dfs(data_file)

        return {"vehicles": vehicles," trajectories": trajectories}
    
    @task()
    def load_data(df):
        db = Database()
        db.vehicle_dataframe_to_sql(df["vehicles"])
        db.trajectory_dataframe_to_sql(df["trajectories"])

   
    df = preprocess_data()
    load_data(df)

preprocess_load_data()