from algorithms import encode, decode, Point
from random import randint
from typing import Tuple
from algorithms import Residue
# gamma: y^2 = x^3 + ax + b (mod q)

N: int  # #gamma
n: int # N = n * h
N = 6
n = 3
h = N // n # ????????????????
# P = tuple(input())
a_, b_, q = -7, 10, 127  #gamma
check_discriminant = (4*a_**3+27*b_**2 != 0)


def bob_first(P: 'Point') -> Tuple['Point', 'Point']:
    if not check_discriminant:
        raise Exception("The curve has self-intersections!")
    d_B = randint(1, n - 1)
    G = Point(0, 0, 0, 0)
    while G.x == 0 and G.y == 0:
        G = P.multiply_point_const(h)
    print("P", P)
    print("G", G.x)
    # G.x = Residue(G.x.number, q)
    # G.y = Residue(G.y.number, q)
    H_B = G.multiply_point_const(d_B)
    # print("G", G, "H_B", H_B)
    return G, H_B


def alice_encrypt(message: str, G: 'Point', H_B: 'Point') -> Tuple['Point', 'Point', int]:
    # a, b = Residue(a_, q), Residue(b_, q)
    M, k = encode((a_, b_, q), message)
    M.x = Residue(M.x, q)
    M.y = Residue(M.y, q)
    print("Encoded msg:", M)
    d_A = randint(1, n - 1)
    H_A = G.multiply_point_const(d_A)
    S = M + H_B.multiply_point_const(d_A)
    return H_A, S, k


def bob_decrypt(H_A, S, k, d_B):
    M = S - H_A.multiply_point_const(d_B)
    num = decode(M, k)
    return num

if __name__ == "__main__":
    x = Residue(2, 127)
    y = Residue(7, 127)
    recieved = bob_first(Point(x, y, a_, b_))
    print("Alice:\n", alice_encrypt('i', recieved[0], recieved[1]))


