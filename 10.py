import math

prime_sum = 0
new_primes = [2,3,5]


max_val = 2000000
max_sieve_val = int(math.ceil(math.sqrt(max_val)))
print('sieve up to', max_sieve_val)

sieve = range(2,max_val)


while True:
    # start by sieving the new primes
    for prime in new_primes:
        print('sieving with ', prime)
        sieve = list(filter(lambda x: x%prime != 0, sieve))

        if prime > max_sieve_val:
            # at this point, all values in sieve are primes, so clean up
            prime_sum += sum(new_primes)
            prime_sum += sum(sieve)
            sieve = []
            break
    else:
        # didn't break
        prime_sum += sum(new_primes)
        # determine what values left in the sieve are definitely prime
        max_prime = max(new_primes)
        # print('max is now: ', max_prime)
        new_primes = list(filter(lambda x : x < max_prime**2, sieve))
        # print(sieve[0:20])
        # print('new primes', new_primes)
        sieve = list(filter(lambda x : x > max_prime**2, sieve))
    
    if len(sieve) == 0:
        break



print(prime_sum)
