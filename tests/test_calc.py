from math import pi
from unittest import TestCase

from calc import sqrt, tan, cos, sin, main


class TestCalc(TestCase):
    def test_sqrt(self):
        self.assertAlmostEqual(2, sqrt(4), 5)

    def test_sqrt_0(self):
        self.assertAlmostEqual(0, sqrt(0), 5)

    def test_sqrt_neg(self):
        self.assertRaises((ValueError, AssertionError), sqrt, -1)

    def test_tan(self):
        self.assertAlmostEqual(0, tan(pi), 5)

    def test_cos(self):
        self.assertAlmostEqual(-1, cos(pi), 5)

    def test_sin(self):
        self.assertAlmostEqual(0, sin(pi), 5)

    def test_main_sqrt(self):
        self.assertAlmostEqual(2, main("sqrt(4)"), 5)

    def test_main_sqrt_0(self):
        self.assertAlmostEqual(0, main("sqrt(0)"), 5)

    def test_main_sqrt_neg(self):
        self.assertRaises((ValueError, AssertionError), main, "sqrt(-1)")

    def test_main_tan(self):
        self.assertAlmostEqual(0, main(f"tan({pi})"), 5)

    def test_main_cos(self):
        self.assertAlmostEqual(-1, main(f"cos({pi})"), 5)

    def test_main_sin(self):
        self.assertAlmostEqual(0, main(f"sin({pi})"), 5)
