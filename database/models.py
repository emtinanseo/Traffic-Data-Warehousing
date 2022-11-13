from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

# class Vehicle defines a postgres table vehicles
class Vehicle(Base):
    __table_name__ = "vehicles"
    id = Column(Integer, primary_key= True) #id is set as the table primary key
    track_id = Column(Integer) 
    type = Column(String)
    traveled_d = Column(Float)
    avg_speed = Column(Float)

    def __repr__(self):
        return "<Vehicle(track_id= {}, type= '{}', traveled_d= {}, avg_speed= {})>".format(
            self.track_id, self.type, self.traveled_d, self.avg_speed)
