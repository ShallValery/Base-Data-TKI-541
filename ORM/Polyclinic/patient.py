from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base
from schedule import Schedule

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    birth_date = Column(Date)
    gender = Column(String)
    policy = Column(String)

    schedules = relationship('Schedule', back_populates='patient')

    def __init__(self, name: str, birth_date: Date, gender: str, policy: str):
        self.name = name
        self.birth_date = birth_date
        self.gender = gender
        self.policy = policy