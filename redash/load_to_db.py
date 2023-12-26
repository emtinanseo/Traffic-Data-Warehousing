import pandas as pd 
from sqlalchemy import create_engine

veh_df = pd.read_csv("vehicles.csv")
trj_df = pd.read_csv("trajectories.csv")

try:
    engine = create_engine('postgresql://postgres:password@localhost:5433/postgres')
    print('engine was created!')
except:
    print('Error creating engine!')

try:
    veh_df.to_sql('vehicle', engine)
    trj_df.to_sql('trajectory', engine)
except:
    print('Error loading tables!')