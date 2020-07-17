import unittest
from my_mod import enlarge, decimate


class TestMathFunctions(unittest.TestCase):

    def test_enlarge(self):
        self.assertEqual(enlarge(10), 1000)

    def test_decimate(self):
        self.assertEqual(decimate(100), 90)

if __name__ == '__main__':
    unittest.main()
