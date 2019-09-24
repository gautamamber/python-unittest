import unittest
from increment import Increment

class IncrementTest(unittest.TestCase):
    i = Increment()

    def test_current(self):
        self.assertEqual(self.i.current_count(), 0)
    
    def test_increment(self):
        self.assertEqual(self.i.increment_count(), 1)

    def test_clear(self):
        self.assertEqual(self.i.clear_count(), 0)
    
if __name__ == "__main__":
    unittest.main()