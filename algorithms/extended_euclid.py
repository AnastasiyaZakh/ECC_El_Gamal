#!/usr/bin/env python
from typing import Tuple
import unittest


def extended_euclid(a: int, b: int) -> Tuple[int, int, int]:
    if a == 0:
        return b, 0, 1
    g, x1, y1 = extended_euclid(b % a, a)
    return g, y1 - b // a * x1, x1


class TestExtendedEuclid(unittest.TestCase):
    def test_72_25(self):
        self.assertEqual(extended_euclid(72, 25), (1, 8, -23))

    def test_345637_143(self):
        self.assertEqual(extended_euclid(345637, 143), (1, 24, -58009))


if __name__== '__main__':
    unittest.main()
