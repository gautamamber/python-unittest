import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):
    def test_factorial_1(self):
        self.assertEqual(factorial(2), 2)
    
    def test_factorial_2(self):
        self.assertEqual(factorial(3), 6)
    
    # this one is fail

    def test_factorial_3(self):
        self.assertEqual(factorial(10), 45)
    
    def test_factorial_4(self):
        self.assertEqual(factorial(4), 24)
    
if __name__ == "__main__":
    unittest.main()