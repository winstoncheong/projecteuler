n = 600851475143
i = 2

factors = []

while True:
    while n%i == 0:  # remove the factor i as many times as possible
        factors.append(i)
        n //= i
    
    i += 1
    if i == n: # Last factor
        factors.append(i)
        break

print(max(factors))