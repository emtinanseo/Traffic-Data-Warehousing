"""Interact with SQL database via Pandas & SQLAlchemy."""
from sqlalchemy import create_engine
from sqlalchemy.types import Integer, String, Float
import pandas as pd
from config import DATABASE_URI, dir
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))
from scripts.read_data import Reader


class Database:
    """Pandas database client."""

    def __init__(self):
        self.engine = create_engine(DATABASE_URI)

    def vehicle_dataframe_to_sql(self, veh_df, table_name: str="vehicles"):
        """Upload vehicle data to the database with proper dtypes."""
        veh_df.to_sql(
            table_name,
            self.engine,
            if_exists='replace',
            index=False,
            chunksize=500,
            dtype={
                "track_id": Integer,
                "type": String,
                "traveled_d": Float,
                "avg_speed":  Float
            }
        )
        print(f'Loaded {len(veh_df)} rows INTO {table_name} table.')
        # result = f'Loaded {len(veh_df)} rows INTO {table_name} table.'
        # return result
    
    def trajectory_dataframe_to_sql(self, traj_df, table_name: str="trajectories"):
        """Upload trajectory data to database with proper dtypes."""
        traj_df.to_sql(
            table_name,
            self.engine,
            if_exists='replace',
            index=False,
            chunksize=500,
            dtype={
                "id": Integer,
                "track_id": Integer,
                "lat": Float,
                "lon": Float,
                "speed":  Float,
                "lon_acc":  Float,
                "lat_acc":  Float,
                "time":  Float
            }
        )
        print(f'Loaded {len(traj_df)} rows INTO {table_name} table.')
        # result = f'Loaded {len(traj_df)} rows INTO {table_name} table.'
        # return result


    def get_dataframe_from_sql(self, table_name):
        """Create DataFrame form SQL table."""
        table_df = pd.read_sql_table(
            table_name,
            con=self.engine
        )
        result = f'Loaded {len(table_df)} rows FROM {table_name}.'
        print(table_df.info())
        return result

#------------------------------
data_file = dir + "/data/20181024_d1_0830_0900.csv" 
def csv_to_sql(data_file:str = data_file):
    reader = Reader()
    db = Database()

    veh_df, traj_df = reader.data_dfs(data_file)
    db.vehicle_dataframe_to_sql(veh_df)
    db.trajectory_dataframe_to_sql(traj_df)


#---------------------------

if __name__ == "__main__":
    data_file = dir + "/data/20181024_d1_0830_0900.csv" 

    csv_to_sql(data_file)