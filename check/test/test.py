# test.py
import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dummytest.main import Calculator

class TestAddition(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_addition_with_negative_numbers(self):
        self.assertEqual(-1 + 1, 0)

if __name__ == '__main__':
    unittest.main()
