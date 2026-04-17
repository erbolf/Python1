import unittest
from main1 import check_even

class TestLogic(unittest.TestCase):

    def test_even(self):
        self.assertTrue(check_even(2))

    def test_odd(self):
        self.assertFalse(check_even(3))

if __name__ == "__main__":
    unittest.main()