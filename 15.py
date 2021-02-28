def binom(n, m):
    from math import factorial as fac
    return fac(n) // fac(m) // fac(n-m)

print(binom(40, 20))
