import argparse
from random import randint
from math import gcd
import time


# Sieve of Eratosthenes
def primes(n):
    b = [True] * (n + 1)
    ps = []
    for p in range(2, n + 1):
        if b[p]:
            ps.append(p)
            for i in range(p ** 2, n + 1, p):
                b[i] = False
    return ps


# Finds modular inverse
# Returns inverse, unused helper and gcd
def modular_inv(a, b):
    if b == 0:
        return 1, 0, a
    q, r = divmod(a, b)
    x, y, g = modular_inv(b, r)
    return y, x - q * y, g


# Addition in Elliptic curve modulo m space
def elliptic_add(p, q, a, b, m):
    # If one point is infinity, return other one
    if p[2] == 0: return q
    if q[2] == 0: return p
    if p[0] == q[0]:
        if (p[1] + q[1]) % m == 0:
            return 0, 1, 0  # Infinity
        num = (3 * p[0] * p[0] + a) % m
        denom = (2 * p[1]) % m
    else:
        num = (q[1] - p[1]) % m
        denom = (q[0] - p[0]) % m
    inv, _, g = modular_inv(denom, m)
    # Unable to find inverse, arithmetic breaks
    if g > 1:
        return 0, 0, denom  # Failure
    z = (num * inv * num * inv - p[0] - q[0]) % m
    return z, (num * inv * (p[0] - z) - p[1]) % m, 1


# Multiplication (repeated addition and doubling)
def elliptic_mul(k, p, a, b, m):
    r = (0, 1, 0)  # Infinity
    while k > 0:
        # p is failure, return it
        if p[2] > 1:
            return p
        if k % 2 == 1:
            r = elliptic_add(p, r, a, b, m)
        k = k // 2
        p = elliptic_add(p, p, a, b, m)
    return r


# Lenstra's algorithm for factoring
# Limit specifies the amount of work permitted
def lenstra(n, limit=10**5):
    start = time.time()
    g = n
    while g == n:
        # Randomized x and y
        q = randint(0, n - 1), randint(0, n - 1), 1
        # Randomized curve coefficient a, computed b
        a = randint(0, n - 1)
        b = (q[1] * q[1] - q[0] * q[0] * q[0] - a * q[0]) % n
        g = gcd(4 * a * a * a + 27 * b * b, n)  # singularity check
    # If we got lucky, return lucky factor
    if g > 1:
        end = time.time()
        duration = end - start
        print(f'execution took {duration} seconds')
        return g, duration
    # increase k step by step until lcm(1, ..., limit)
    for p in primes(limit):
        pp = p
        while pp < limit:
            q = elliptic_mul(p, q, a, b, n)
            # Elliptic arithmetic breaks
            if q[2] > 1:
                end = time.time()
                duration = end - start
                print(f'execution took {duration} seconds')
                return gcd(q[2], n), duration
            pp = p * pp
    end = time.time()
    duration = end - start
    print(f'execution took {duration} seconds')
    return False, duration


from collections import Counter


def get_factor(n: int, limit) -> int:
    pass


def simple_factorize(n: int) -> Counter:
    pass  # simple factorization algorithm here


def factorize(n: int, threshold) -> Counter:
    if n < threshold:
        return simple_factorize(n)
    f1 = get_factor(n)
    f2 = n // f1
    return factorize(f1) + factorize(f2)


def main():
    # parser = argparse.ArgumentParser(description='Process arguments')
    # parser.add_argument('--n', type=int, help='number to factor')
    # parser.add_argument('--limit', type=int, default=1000,
    #                     help='work limit (default = 1000)')
    # args = parser.parse_args()

    # print(lenstra(args.n, args.limit))
    print(lenstra(55555555555855555, 5000000))


if __name__ == '__main__':
    main()
