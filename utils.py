
def prod_list(lst):
    """Returns the product of all elements of the list passed in"""

    from operator import mul
    from functools import reduce
    
    return reduce(mul, lst, 1)

def factorial(n):
    """Returns n!"""

    return prod_list(range(1, n+1))

def sum_digits(number):
    """Sums the digits of a given number"""
    return sum(map(int, list(str(number))))


if __name__ == "__main__":
    print(factorial(5))