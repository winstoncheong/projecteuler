primes = [2, 3, 5]

cur = max(primes) + 1

while len(primes) < 10001:
    for p in primes:
        if cur % p == 0:
            break

    else: # didn't hit break, so all primes failed to divide cur
        primes.append(cur)
        # print('Found prime:', cur)

    cur += 1

print(primes[-1])