from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from base import Base

class Cabinet(Base):
    __tablename__ = 'cabinets'

    id = Column(Integer, primary_key=True, index=True)

    schedules = relationship('Schedule', back_populates='cabinet')
