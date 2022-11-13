# file for CRUD operation on our database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from config import DATABASE_URI

engine = create_engine(DATABASE_URI)

# Create a global Session object, which is a factory for individual sessions 
Session = sessionmaker(bind=engine)

# Create individual sessions off of the global Session:
#s = Session()


def recreate_database():
    """
     a function to recreate the database
     assuming we have an engine in the global scope, which is usually the case.
    """
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

# ------------------------------------------- cli.py
# from crud import Session
# from models import Vehicle, Trajectory

#recreate_database() # empty the db
#s = Session()
# # Add a vehicle to vehicles table
# vehicle = Vehicle(track_id= 1, type='Car',traveled_d=0, avg_speed=0)

# s.add(vehicle) # add vehicle object/row to Vehicle model (vehicles table)

# vehicles = s.query(Vehicle).all()

# for veh in vehicles:
#     print(veh.type)

# s.commit()

# s.close()