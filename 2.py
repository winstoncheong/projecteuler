i = 1
j = 2

even_fib = []

while i <= 4000000:
    if i%2 == 0:
        even_fib.append(i)
    i,j = j, i+j

print(sum(even_fib))