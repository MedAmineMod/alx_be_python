import unittest

from simple_calculator import SimpleCalculator

simple =  SimpleCalculator()

class TestSimpleCalculator(unittest.TestCase) : 

    def setUp(self) -> None:
        self.calc = SimpleCalculator()
    

    def test_addition(self) :
        
        self.assertEqual(self.calc.add(5,5)  , 10)

    def test_subtraction(self) :
        
        self.assertEqual(self.calc.subtract(5,5) , 0)
    
    def test_multiplication(self) :
       
        self.assertEqual(self.calc.multiply(5,5) , 25)

    def test_division(self) :
        self.assertIsNone(self.calc.divide(5,0))
        self.assertEqual(self.calc.divide(5,5) , 1)


        
