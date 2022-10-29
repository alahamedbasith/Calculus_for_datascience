# import sympy 
from sympy import *

x, y = symbols('x y') 
expr = x**2 + 10 * y + y**3
print("Expression : {} ".format(expr)) 

# Use sympy.Derivative() method 
expr_diff = Derivative(expr, x) 
  
Print ("Etymology of expression with respect to x: {}". Format. (Expr_diff)
print("Value of the derivative : {} ".format(expr_diff.doit())) 
