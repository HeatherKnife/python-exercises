"""
A collection of simple math operations
"""

def simple_add(a,b):
    return a+b

    """This function recieves two arguments and add them
    
    Parameters
    ----------
    a : float 
    b : float

    Returns
    -------
    returns a float wich is result of the addition of the two parameters 

    """

def simple_sub(a,b):
    return a-b

       """This function recieves two arguments of any type and return the
    substraction of them"""

def simple_mult(a,b):
    return a*b

def simple_div(a,b):
    return a/b

def poly_first(x, a0, a1):
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
