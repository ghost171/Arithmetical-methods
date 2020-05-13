import numpy as np
import scipy.linalg as sl

def f(x):
    return 1 + 12 * x * x

n = 10

u = np.array([0] + [0] + [ -1] * (n -1))
d = np.array([1] + [2] * (n - 1) + [1])
l = np.array ([ -1] * (n - 1) + [0] + [0])
A = np.array([ u , d , l ])
h = 1.0 / n
x = np.linspace (0 , 1 , n + 1)
b = h * h * np.vectorize(f)(x)
b[0] = 1
b[n] = 1
y = sl.solve_banded((1 , 1) , np.array([ u , d , l ]), b )
print(y)