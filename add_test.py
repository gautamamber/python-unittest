import unittest
from add import add

class AddTestCase(unittest.TestCase):
    def test_add_1(self):
        self.assertEqual(add(2,3), 5)
    
    def test_add_2(self):
        self.assertEqual(add(2,6), 8)
    
    #this will fail

    def test_add_3(self):
        self.assertEqual(add(2,3), "six")
    
    def test_add_4(self):
        self.assertEqual(add(100, 200), 300)
    
if __name__ == "__main__":
    unittest.main()
