import typing as tp
import unittest
from algorithms import Residue


class Point:
    _x: Residue
    _y: Residue
    _a: int
    _b: int

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, var):
        self._x = var

    @y.setter
    def y(self, var):
        self._y = var

    def __init__(self, x, y, a: float, b: float) -> None:
        self._x, self._y, self._a, self._b = x, y, a, b

    def __str__(self) -> str:
        return f"Point({self._x},{self._y})"

    def __repr__(self) -> str:
        return f"Point({self._x},{self._y}) on the curve y^2=x^3{self._a:+}x{self._b:+}"

    def __eq__(self, other: 'Point') -> bool:
        return self._x == other._x and self._y == other._y and \
               self._a == other._a and self._b == other._b

    def __neg__(self) -> 'Point':
        return Point(self._x, -self._y, self._a, self._b)

    def __sub__(self, other: 'Point') -> 'Point':
        return self + (-other)

    def __isub__(self, other: 'Point') -> 'Point':
        self = self - other
        return self

    def __add__(self, other: 'Point') -> 'Point':
        if other is None:
            return self
        if other._x == 0 and other._y == 0:
            return self
        if self._x == 0 and self._y == 0:
            return other
        assert self._a == other._a and self._b == other._b

        if self._x == other._x:
            if self._y + other._y == 0:
                return Point(0, 0, self._a, self._b)
            else:  # y1 = y2, Point_1 = Point_2
                k = (3 * self._x ** 2 + self._a) / (2 * self._y)
        else:
            k = (other._y - self._y) / (other._x - self._x)

        # if self == other:
        #     k = (3 * self._x ** 2 + self._a) / (2 * self._y)
        # else:
        #     k = (self._y - other._y) / (self._x - other._x)

            # try:
            #     k = (self._y - other._y) / (self._x - other._x)
            # except:
            #     return Point(0, 0, self._a, self._b)
        res_x = k ** 2 - self._x - other._x
        res_y = self._y + k * (res_x - self._x)
        return Point(res_x, -res_y, self._a, self._b)

    def __radd__(self, other: tp.Optional['Point']) -> 'Point':
        if other is None:
            return self
        return self + other

    def __iadd__(self, other: tp.Optional['Point']) -> 'Point':
        self = self + other
        return self

    def multiply_point_const(self, c: int) -> 'Point':
        sign = 1
        if c < 0:
            c = abs(c)
            sign = -1
        coefficients = [int(bit) for bit in bin(c)[:1:-1]]
        res = None
        for power, coefficient in enumerate(coefficients):
            if coefficient:
                res += self.double(power)
        if sign == 1:
            return res
        elif sign == -1:
            return -res

    def double(self, pow: int):
        point = self
        for _ in range(pow):
            point += point
        return point


class TestPointMath(unittest.TestCase):

    def test_multiply_point_const(self):
        '''
        P=(2, 7)
        2P=(5, 2)
        3P=(8, 3)
        12P=(2, 4)
        13P=(0, 0)
        '''
        x = Residue(2, 11)
        y = Residue(7, 11)
        p = Point(x, y, 1, 6)
        coefficient = 10
        res = Point(8, 8, 1, 6)
        self.assertEqual(p.multiply_point_const(coefficient), res)

    def test_add_simple(self):
        # y^2 = x^3 - 7 x + 10
        a, b = -7, 10
        p = Point(1, 2, a, b)
        q = Point(0, 0, a, b)
        r = Point(1, 2, a, b)
        self.assertEqual(p + q, r)

    def test_add_3(self):
        x = Residue(2, 11)
        y = Residue(7, 11)
        x_1 = Residue(2, 11)
        y_1 = Residue(4, 11)
        p = Point(x, y, 1, 6)
        q = Point(x_1, y_1, 1, 6)
        r = Point(0, 0, 1, 6)
        self.assertEqual(p + q, r)

    def test_add_more(self):
        # y^2 = x^3 - 7 x + 10
        a, b = -7, 10
        p = Point(1, 2, a, b)
        q = Point(5, 10, a, b)
        r = Point(-2., 4., a, b)
        self.assertEqual(p + q, r)

    def test_add_same(self):
        # y^2 = x^3 - 7 x + 10
        a, b = 1, 6
        x = Residue(2, 11)
        y = Residue(7, 11)
        p = Point(x, y, a, b)
        q = Point(x, y, a, b)
        r = Point(5, 2, a, b)
        self.assertEqual(p + q, r)

    def test_add_none(self):
        # y^2 = x^3 - x + 6
        a, b = 1, 6
        x = Residue(2, 11)
        y = Residue(7, 11)
        p = Point(x, y, a, b)
        q = None
        r = p
        self.assertEqual(p + q, r)

    def test_mul_for_lenstra(self):
        #  y^2 = x^3 + 5x - 5
        a, b = 5, -5
        p = Point(1, 1, a, b)
        c = 2
        res = Point(14, -53, a, b)
        self.assertEqual(p.multiply_point_const(c), res)

    # def test_mult_simple(self):
    #     # y^2 = x^3 + 2 x + 7
    #     a, b = -7, 10
    #     p = Point(1, 2, a, b)
    #     c = 2
    #     r = Point(-1., -4., a, b)
    #     self.assertEqual(c * p, r)
    #
    # def test_mult_2(self):
    #     # y^2 = x^3 + x + 6
    #     a, b = -7, 10
    #     p = Point(1, 2, a, b)
    #     c = 2
    #     r = Point(-1., -4., a, b)
    #     self.assertEqual(c * p, r)
    #
    # def test_mult_more(self):
    #     # y^2 = x^3 - 7 x + 10
    #     a, b = -7, 10
    #     p = Point(1, 2, a, b)
    #     c = 3
    #     r = Point(9., -26., a, b)
    #     self.assertEqual(c * p, r)

    # def test_mult_a_lot_more(self):
    #     # y^2 = x^3 - 7 x + 10
    #     a, b = -7, 10
    #     p = Point(1, 2, a, b)
    #     c = 1024
    #     r = Point(20.16778, 89.84352, a, b)
    #     q = c * p
    #     self.assertAlmostEqual(q._x, r._x, 5)
    #     self.assertAlmostEqual(q._y, r._y, 5)

    # def test_mult_1(self):
    #     # y^2 = x^3 + 1 x + 6
    #     a, b = 1, 6
    #     p = Point(2, 7, a, b)
    #     c = 2
    #     r = Point(5., 2., a, b)
    #     self.assertEqual(c * p, r)

    # def test_add_1(self):
    #     # y^2 = x^3 + 2 x + 3
    #     a, b = 2, 3
    #     p = Point(3, 6, a, b)
    #     q = Point(3, 6, a, b)
    #     r = Point(80., 10., a, b)
    #     self.assertEqual(p + q, r)


if __name__ == '__main__':
    unittest.main()

    # x = Residue(5, 11)
    # y = Residue(9, 11)
# x_1 = Residue(5, 11)
# y_1 = Residue(2, 11)
#     p = Point(x, y, 1, 6)
# q = Point(x_1, y_1, 1, 6)
# try: a = (p+q)
# except: a = (Point(0,0,1,6))
# # r = Point(0, 0, 1, 6)
# print(p+q)
