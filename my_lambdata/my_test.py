import unittest
from my_mod import enlarge, decimate


# def enlarge(number: float) -> float:
#     '''
#     Created in class, this multiplies
#     a number given by 100.
#     '''
#     return number * 100


# def decimate(number: float) -> float:
#     '''
#     Decimates a given number (reduces
#     by 10%)
#     '''
#     return number - (number * .1)


class TestMathFunctions(unittest.TestCase):

    def test_enlarge(self):
        self.assertEqual(enlarge(10), 1000)

    def test_decimate(self):
        self.assertEqual(decimate(100), 90)

if __name__ == '__main__':
    unittest.main()
