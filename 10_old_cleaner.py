from math import sqrt, ceil

TOP = 2000000
sieve = range(2,TOP)

toSieve = [2]
i = 3
while i < ceil(sqrt(TOP)):
  # check if i is prime
  isprime = True
  for p in toSieve:
    if i % p == 0:
      isprime = False
      break
  if isprime:
    toSieve.append(i)

  i += 2 # only odds
print(toSieve)

for i in toSieve:
  # keep the ones for which the filter is true
  sieve = list(filter(lambda x : x == i or x % i != 0, sieve))
  # print(sieve)
  print("filtered the number " + str(i))


print(sum(sieve))
