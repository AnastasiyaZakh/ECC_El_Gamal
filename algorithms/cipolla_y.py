#!usr/bin/env python3
from sympy.ntheory import legendre_symbol
# x^2 = a (mod p) --> x


def cipolla(a: int, p: int) -> str:
    if legendre_symbol(a, p) == -1:
        return 'Немає розв*язку'
    elif legendre_symbol(a, p) == 1:
        for t in range(1, p-1):
            v = t ** 2 - a
            if legendre_symbol(v, p) == -1:
                break
        y = 1
        t1, y1 = t, y
        for power in range(1, int((p+1)/2)):
            t1, y1 = (t1 * t + y1 * y * v) % p, (t1 * y + t * y1) % p
    return t1


# print(f'x = ±{cipolla( int(input("a:")) , int(input("p:")) )}')
# 132760, 179 -> 168
