from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class Doctor(Base):
    __tablename__ = 'doctors'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    birth_date = Column(Date)
    gender = Column(String)
    specialization_id = Column(Integer, ForeignKey('specializations.id'))

    patients = relationship('Patient', back_populates='doctor')
    schedules = relationship('Schedule', back_populates='doctor')
    specialization = relationship('Specialization', back_populates='doctors')

    def __init__(self, name: str, birth_date: Date, gender: str, specialization_id: int):
        self.name = name
        self.birth_date = birth_date
        self.gender = gender
        self.specialization_id = specialization_id
