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

class TestCabinet(unittest.TestCase):
    def setUp(self):
        self.cabinet = Cabinet(101)

    def test_init(self):
        self.assertEqual(self.cabinet.id, 101)

if __name__ == '__main__':
    unittest.main()
