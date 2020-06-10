#!/usr/bin/env python3
from typing import Tuple
from random import randint
from algorithms import Point, Residue


E: Tuple[int, int]
N: int
P: Point
P = Point(E[0], E[1], )
h: None  # hash-func

# Z_n = lambda n: list(range(1, n))


def concat(point: Point):
    return int(''.join([str(point.x), str(point.y)]))


def mk_sign(N: int, P: Point, text) -> Tuple[Point, int, Point]:
    k = randint(1, N)
    Y = P.multiply_point_const(k)
    r = randint(0, N - 2)
    C = P.multiply_point_const(r)
    d = ((1 / r) * (hash(text) - k * hash(concat(C)))) % N
    return C, d, Y


def check_sign(text, P: Point, Y: Point, C: Point, d: int) -> bool:
    U = Y.multiply_point_const(hash(concat(C))) + C.multiply_point_const(d)
    V = P.multiply_point_const(hash(text))
    return U == V


if __name__ == "__main__":
    E = (-7, 10)  # EC
    x = Residue(5, 127)
    y = Residue(10, 127)
    P = Point(x, y, E[0], E[1])

    print(mk_sign(0, 0, 'aasasas'))
