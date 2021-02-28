
def sum_of_digits(n):
    return sum(map(int, list(str(n))))

#print(sum_of_digits(2**15))
print(sum_of_digits(2**1000))