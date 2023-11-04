from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base

class Specialization(Base):
    __tablename__ = 'specializations'

    id = Column(Integer, primary_key=True, index=True)
    specialization = Column(String)

    doctors = relationship('Doctor', back_populates='specialization')

    def __init__(self, specialization: str):
        self.specialization = specialization
