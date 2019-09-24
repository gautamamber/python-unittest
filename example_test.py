import unittest

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        pass

    # check and return string contains multiple

    def test_string_a(self):
        self.assertEqual("a"*7, "aaaaaaa")
    
    def test_string_upper(self):
        self.assertTrue("HELLO".isupper())
        self.assertFalse("hello".isupper())
    
    def test_strip(self):         
        s = 'geeksforgeeks'
        self.assertEqual(s.strip('geek'), 'sforgeeks') 
    
if __name__ == "__main__":
    unittest.main()
    
