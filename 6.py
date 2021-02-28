
def triangle_num(n):
    return n*(n+1)//2

def sum_of_squares(n):
    return n*(n+1)*(2*n+1)//6


# print(sum_of_squares(10))
# print(triangle_num(10)**2)
print(triangle_num(100)**2 - sum_of_squares(100))