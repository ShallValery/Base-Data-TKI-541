from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class Schedule(Base):
    __tablename__ = 'schedules'

    id = Column(Integer, primary_key=True, index=True)
    datetime = Column(DateTime)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    cabinet_id = Column(Integer, ForeignKey('cabinets.id'))

    patient = relationship('Patient', back_populates='schedules')
    doctor = relationship('Doctor', back_populates='schedules')
    cabinet = relationship('Cabinet', back_populates='schedules')

    def __init__(self, datetime: DateTime, patient_id: int, doctor_id: int, cabinet_id: int):
        self.datetime = datetime
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.cabinet_id = cabinet_id