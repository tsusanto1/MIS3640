import math

def quadratic(a, b, c): 
    xOne = (-b + math.sqrt(b**2-4*a*c))/(2*a)
    xTwo = (-b - math.sqrt(b**2-4*a*c))/(2*a)
    print("The values of x are " + xOne + " " + xTwo)
quadratic(3, -5, -8)
