import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
# Our integral approximation function
def integral_approximation(f, a, b):
    return (b-a)*np.mean(f)
# Integrate f(x) = x^2
def f1(x):
    return x**2
# Define bounds of integral
a = 0
b = 1
# Generate function values
x_range = np.arange(a,b+0.0001,.0001)
fx = f1(x_range)
# Approximate integral
approx = integral_approximation(fx,a,b)
print(approx)
