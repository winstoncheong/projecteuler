import math

def lcm(a, b):
    return a*b // math.gcd(a,b)

res = 1
for i in range(2, 21):
    res = lcm(res, i)

print(res)
