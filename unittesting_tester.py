"""
    Unit Testing

Author: Ana M. Almeida
Date: 24.10.2022

Guide: https://github.com/anamvalmeida/courses/blob/Applied-AI/UnitTesting_v2.pdf
"""

import unittest

from unittesting import square, double, add

class TestSquare(unittest.TestCase):
    def test1(self):
        self.assertEqual(square(2),4)
        self.assertEqual(square(3),9)
        self.assertNotEqual(square(-3),-9)

class TestDouble(unittest.TestCase):
    def test1(self):
        self.assertEqual(double(2),4)
        self.assertEqual(double(-3.1),-6.2)
        self.assertEqual(double(0),0)

# unittest.main()

# FAILED in the last line indicates that at least one
# test has failed, and python prints which test or tests failed.

class TestAdd(unittest.TestCase):
    def test1(self):
        self.assertEqual(add(1,2),3)
        
unittest.main()
