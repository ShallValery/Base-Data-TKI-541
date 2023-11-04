from sqlalchemy import Column, Integer, Time
from sqlalchemy.orm import relationship
from base import Base

class Time(Base):
    __tablename__ = 'times'

    id = Column(Integer, primary_key=True, index=True)
    time = Column(Time)

    schedules = relationship('Schedule', back_populates='time')

    def __init__(self, time: Time):
        self.time = time
