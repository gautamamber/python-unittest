import unittest
class NotEqualTest(unittest.TestCase):
    # pass
    def  test_not_equal(self):
        self.assertNotEqual(2, (2-2))
    
    # fail
    def  test_not_equal_2(self):
        self.assertNotEqual(2, (4-2))
    
if __name__ == "__main__":
    unittest.main()