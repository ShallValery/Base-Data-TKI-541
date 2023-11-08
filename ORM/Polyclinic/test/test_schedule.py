import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from datetime import datetime
from patient import Patient
from schedule import Schedule
from doctor import Doctor
from cabinet import Cabinet
from specialization import Specialization

class TestSchedule(unittest.TestCase):
    def setUp(self):
        self.schedule = Schedule(datetime.now(), 1, 1, 1)

    def test_init(self):
        self.assertEqual(self.schedule.patient_id, 1)
        self.assertEqual(self.schedule.doctor_id, 1)
        self.assertEqual(self.schedule.cabinet_id, 1)

if __name__ == '__main__':
    unittest.main()
