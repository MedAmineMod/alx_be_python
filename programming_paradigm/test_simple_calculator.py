import unittest

from simple_calculator import SimpleCalculator

simple =  SimpleCalculator()

class TestSimpleCalculator(unittest.TestCase) : 

    def test_add(self) :
        result = simple.add(5 ,5 )
        self.assertEqual(result , 10)

    def test_subtract(self) :
        result = simple.subtract(5 ,5 )
        self.assertEqual(result , 0)
    
    def test_multiply(self) :
        result = simple.multiply(5 ,5 )
        self.assertEqual(result , 25)

    def test_divide(self) :
        result = simple.divide(5 ,5 )
        self.assertEqual(result , 1)