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
        """Upload data to database with proper dtypes."""
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
        result = f'Loaded {len(veh_df)} rows INTO {table_name} table.'
        print(result)
        return result

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

    veh_df, _ = reader.data_dfs(data_file)
    x= db.vehicle_dataframe_to_sql(veh_df)
    print(x)

#---------------------------

if __name__ == "__main__":
    data_file = dir + "/data/20181024_d1_0830_0900.csv" 

    csv_to_sql(data_file)