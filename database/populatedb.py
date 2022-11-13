"""Interact with SQL database via Pandas & SQLAlchemy."""
from sqlalchemy import create_engine
from sqlalchemy.types import Integer, String, Float
import pandas as pd
from config import DATABASE_URI


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