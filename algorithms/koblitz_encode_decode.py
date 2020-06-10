#!/usr/bin/env python3
from sympy.ntheory import legendre_symbol
from algorithms import cipolla_y, Point
from typing import Tuple
import math

# ord('~')=126
# chr(126)='~'

base = 1 << 16

def text_to_num(text: str) -> int:
    a = list(map(ord, text))  # list of UNICODE dots
    # num = 0
    # for k, a_k in enumerate(a, start=1):
    #     num = num + a_k * base ** (k - 1)
    n = len(a)
    num = sum([a[k] * base ** k for k in range(n)])
    return num

def num_to_text(number: int) -> str:
    coefficients = []
    while number:
        coefficients.append(number % base)
        number //= base
    characters = list(map(chr, coefficients))
    return ''.join(characters)

def num_to_point(a, b, p: int, m: int) -> Tuple['Point', int]:
    # m = text_to_num(text)
    k = p // (m + 1)
    # print("k =", k)
    x, y = 0, 0
    for j in range(k + 1):
        x = m * k + j
        if legendre_symbol(x ** 3 + a * x + b, p) == 1:
            y = cipolla_y.cipolla(x ** 3 + a * x + b, p)
            break
    return Point(x, y, a, b), k

def point_to_num(p: 'Point', k) -> int:
    return p.x // k

def encode(curve: tuple, text: str) -> Tuple['Point', int]:
    a, b, p = curve[0], curve[1], curve[2]
    num = text_to_num(text)
    return num_to_point(a, b, p, num)

def decode(point: Point, k: int) -> str:
    num = point_to_num(point, k)
    return num_to_text(num)


if __name__ == "__main__":
    # p = (2**128-3)/76439
    # print(p)
    p = int('DB7C2ABF62E35E668076BEAD208B', 16)
    a = int('DB7C2ABF62E35E668076BEAD2088', 16)
    b = int('659EF8BA043916EEDE8911702B22', 16)
    G = Point(int('09487239995A5EE76B55F9C2F098', 16),
              int('A89CE5AF8724C0A23E0E0FF77500', 16), a, b)
    n = int('DB7C2ABF62E35E7628DFAC6561C5', 16)
    h = int('01', 16)
    a = -7
    b = 10
    p = 487

    print(h)
    new_point = encode((a, b, p), 'aaa')
    print(new_point)
# y^2=x^3+2x+7(mod 179)

# print(num_to_point(-7, 10, 127, 'a'))
# m1 = 3160918205608148134863399242437668999277801104545742920
# print(f'Hello World -> %s' % text_to_num('Hello World!') )
# print(f'm -> %s' % num_to_text(m1))


# num = text_to_num('a')
# g_p = num_to_point(-7, 10, 127, num)
# print("Point from 'a':", g_p[0])
# print("Number:", point_to_num(g_p[0], g_p[1]))
# print("Finally:", encode( (-7, 10, 127), 'a'))
# point = encode( (-7, 10, 127), 'a')
# decoded = decode(point[0], point[1])
# print(f"decoded from {point[0]}", decoded)

# def koblitz_encode(a: int, b: int, p: int, text: str) -> tuple:
#     base = 1 << 16
#     unicode_symb = list(map(ord, text))  # list of UNICODE dots
#     n = len(unicode_symb)
#     num = sum([unicode_symb[k] * base ** k for k in range(n)])
#     d = min(p // num, 100)
#     for j in range(d):
#         x = (d * num + j) % p
#         s = (x ** 3 + a * x + b) % p
#         if s ** ((p + 1) / 2) % p == s % p:
#             y = s ** ((p + 1) / 4) % p
#             return x, y
# print(koblitz_encode(-7, 10, 127, 'a'))

# def koblitz_decode(P):
#     b = 2 ** 16
#     d = 100
#     lst = []
#     m = P[0] // d  # (P[0]/P[2]) represents the x-coordinate of the point.
#     while m != 0:
#         lst.append(chr(m % b)) #converts m to a list of characters
#         Nmb //= b #replaces Nmb by floor(Nmb/b)
#     return ''.join(lst)
