import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from datetime import datetime, date
from patient import Patient
from schedule import Schedule
from doctor import Doctor
from cabinet import Cabinet
from specialization import Specialization

class TestCabinet(unittest.TestCase):
    def setUp(self):
        self.cabinet = Cabinet(101)

    def test_init(self):
        self.assertEqual(self.cabinet.id, 101)

class TestDoctor(unittest.TestCase):
    def setUp(self):
        self.doctor = Doctor('Доктор Хаус', date(1980, 1, 1), 'М', 1)

    def test_init(self):
        self.assertEqual(self.doctor.name, 'Доктор Хаус')
        self.assertEqual(self.doctor.birth_date, date(1980, 1, 1))
        self.assertEqual(self.doctor.gender, 'М')
        self.assertEqual(self.doctor.specialization_id, 1)

class TestPatient(unittest.TestCase):
    def setUp(self):
        self.patient = Patient('Иван Иванов', date(1980, 1, 1), 'М', '1234567890')

    def test_init(self):
        self.assertEqual(self.patient.name, 'Иван Иванов')
        self.assertEqual(self.patient.birth_date, date(1980, 1, 1))
        self.assertEqual(self.patient.gender, 'М')
        self.assertEqual(self.patient.policy, '1234567890')

class TestSchedule(unittest.TestCase):
    def setUp(self):
        self.schedule = Schedule(datetime.now(), 1, 1, 1)

    def test_init(self):
        self.assertEqual(self.schedule.patient_id, 1)
        self.assertEqual(self.schedule.doctor_id, 1)
        self.assertEqual(self.schedule.cabinet_id, 1)

class TestSpecialization(unittest.TestCase):
    def setUp(self):
        self.specialization = Specialization('Терапевт')

    def test_init(self):
        self.assertEqual(self.specialization.specialization, 'Терапевт')

if __name__ == '__main__':
    unittest.main()
