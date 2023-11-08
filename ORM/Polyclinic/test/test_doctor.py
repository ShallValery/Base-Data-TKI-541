import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from datetime import date
from patient import Patient
from schedule import Schedule
from doctor import Doctor
from cabinet import Cabinet
from specialization import Specialization

class TestDoctor(unittest.TestCase):
    def setUp(self):
        self.doctor = Doctor('Доктор Хаус', date(1980, 1, 1), 'М', 1)

    def test_init(self):
        self.assertEqual(self.doctor.name, 'Доктор Хаус')
        self.assertEqual(self.doctor.birth_date, date(1980, 1, 1))
        self.assertEqual(self.doctor.gender, 'М')
        self.assertEqual(self.doctor.specialization_id, 1)

if __name__ == '__main__':
    unittest.main()
