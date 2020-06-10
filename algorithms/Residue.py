#!usr/bin/env python3
# ax = b (mod m)
# find x
import unittest
import typing as tp


def modular_power(base: int, power: int, modulo: int) -> int:
    result = 1
    while power:
        if power & 1:
            result *= base
            result %= modulo
        base *= base
        base %= modulo
        power >>= 1
    return result


def modular_inverse(number: int, modulo: int) -> int:
    return modular_power(number, modulo - 2, modulo)


class Residue:
    def __init__(self, number: int, modulo) -> None:
        self.number = number % modulo
        self.modulo = modulo

    def __str__(self) -> str:
        return f"{self.number}"

    def __eq__(self, other):
        try:
            return self.number == other.number and self.modulo == other.modulo
        except AttributeError:
            return self.number == other

    def __truediv__(self, other: 'Residue') -> 'Residue':
        assert other.number != 0, "Cannot divide by 0"
        assert self.modulo == other.modulo, "Cannot divide elements of different groups"
        return Residue(self.number * modular_inverse(other.number, other.modulo), self.modulo)

    def __add__(self, other: tp.Union['Residue', int]) -> 'Residue':
        if isinstance(other,int):
            return Residue((self.number + other), self.modulo)
        else:
            return Residue((self.number + other.number), self.modulo)

    def __mul__(self, other: 'Residue'):
        return Residue((self.number * other.number), self.modulo)

    def __rmul__(self, const: int):
        return Residue((const * self.number), self.modulo)

    def __pow__(self, power: int):
        return Residue(self.number ** power, self.modulo)

    def __neg__(self):
        return Residue(-self.number, self.modulo)

    def __sub__(self, other: 'Residue'):
        return Residue((self.number - other.number) % self.modulo, self.modulo)


# class TestModulo(unittest.TestCase):
#
#     def test_eq(self):
#         a = Residue(2, 5)
#         b = 2
#         res = True
#         self.assertEqual(a==b, res)
#
#
#     def test_division(self):
#         # a r = b (mod m)
#         b = Residue(1, 11)
#         a = Residue(3, 11)
#         r = Residue(4, 11)
#         self.assertEqual(b / a, r)
#
#     def test_sum(self):
#         a = Residue(4, 9)
#         b = Residue(8, 9)
#         res = Residue(3, 9)
#         self.assertEqual(a + b, res)
#
#     def test_mul(self):
#         a = Residue(4, 9)
#         b = Residue(8, 9)
#         res = Residue(5, 9)
#         self.assertEqual(a * b, res)
#
#     def test_sub(self):
#         a = Residue(3, 9)
#         b = Residue(5, 9)
#         res = Residue(7, 9)
#         self.assertEqual(a - b, res)
#
#
if __name__ == '__main__':
    unittest.main()
