from sqlalchemy import Column, Integer, Date
from sqlalchemy.orm import relationship
from base import Base

class Date(Base):
    __tablename__ = 'dates'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)

    schedules = relationship('Schedule', back_populates='date')

    def __init__(self, date: Date):
        self.date = date
