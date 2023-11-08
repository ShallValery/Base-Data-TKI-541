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

class TestPatient(unittest.TestCase):
    def setUp(self):
        self.patient = Patient('Иван Иванов', date(1980, 1, 1), 'М', '1234567890')

    def test_init(self):
        self.assertEqual(self.patient.name, 'Иван Иванов')
        self.assertEqual(self.patient.birth_date, date(1980, 1, 1))
        self.assertEqual(self.patient.gender, 'М')
        self.assertEqual(self.patient.policy, '1234567890')

if __name__ == '__main__':
    unittest.main()

