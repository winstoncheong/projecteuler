
def prod_list(lst):
    """Returns the product of all elements of the list passed in"""

    from operator import mul
    from functools import reduce
    
    return reduce(mul, lst, 1)