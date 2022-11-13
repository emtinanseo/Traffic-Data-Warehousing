from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Float

Base = declarative_base()

# class Vehicle defines a postgres table vehicles
class Vehicle(Base):
    __table_name__ = "vehicles"
    #id = Column(Integer, primary_key= True) #id is set as the table primary key
    track_id = Column(Integer, primary_key= True) #track_id is set as the table primary key
    type = Column(String)
    traveled_d = Column(Float)
    avg_speed = Column(Float)
    children = relationship("Trajectory")

    def __repr__(self):
        return "<Vehicle(track_id= {}, type= '{}', traveled_d= {}, avg_speed= {})>".format(
            self.track_id, self.type, self.traveled_d, self.avg_speed)

#['track_id', 'type', 'traveled_d', 'avg_speed', 
# 'lat', 'lon', 'speed', 'lon_acc', 'lat_acc', 'time']

# class Trajectory defines a postgres table trajectories
class Trajectory(Base):
    __table_name__ = "trajectories"
    id = Column(Integer, primary_key= True) #id is set as the table primary key
    track_id = Column(Integer, ForeignKey("vehicles.track_id")) 
    lat =Column(Float)
    lon = Column(Float)
    speed= Column(Float)
    lon_acc = Column(Float)
    lat_acc = Column(Float)
    time= Column(Float)

    def __repr__(self):
        return "<Trajectory(track_id= {}, lat= {}, lon= {}, speed ={}, lon_acc= {}, lat_acc= {}, time= {})>".format(
            self.track_id, self.lat, self.lon, self.speed, self.lon_acc, self.lat_acc, self.time)