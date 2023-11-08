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


class TestSpecialization(unittest.TestCase):
    def setUp(self):
        self.specialization = Specialization('Терапевт')

    def test_init(self):
        self.assertEqual(self.specialization.specialization, 'Терапевт')

if __name__ == '__main__':
    unittest.main()
