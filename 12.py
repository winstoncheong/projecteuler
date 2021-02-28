
def factorize(n):
    """Factorize an integer. Returns a counter that gives primes and their multiplicity"""
    from collections import Counter

    factors = []
    i = 2

    while True:
        while n%i == 0:  # remove the factor i as many times as possible
            factors.append(i)
            n //= i
        
        i += 1
        if i > n: # will only happen when n=1, so found all factors
            break

    ctr = Counter(factors)
    return ctr

def num_divisors(n):
    """Returns the number of divisors of a given number"""
    factorization = factorize(n)
    # print(n, factorization)
    ans = 1
    for powers in factorization.values():
        ans *= powers + 1
    
    return ans

def triangle_num(n):
    return n*(n+1)//2

        
i = 2
num_div = num_divisors(triangle_num(i))
while num_div <= 500:
    i += 1
    # print('trying ', i, triangle_num(i))
    num_div = num_divisors(triangle_num(i))

print(triangle_num(i))