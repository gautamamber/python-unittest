from calculator import  Calculator
import unittest

class TestCalculator(unittest.TestCase):

    c = Calculator(5,0)

    def test_add(self):
        self.assertEqual(self.c.add(), 5)
    
    def test_subtract(self):
        self.assertEqual(self.c.subtract(), 5)

    def test_multiply(self):
        self.assertEqual(self.c.multiply(), 0)
    
    def test_division(self):
        self.assertEqual(self.c.division(), False)
    
if __name__ == "__main__":
    unittest.main()
