import numpy as np
from scipy.linalg import solve_banded


def sweep ( a, b, c, f, n):
    alpha = (n + 1) * [0]
    beta = (n + 1) * [0]
    x = n * [0]
    a[0] = 0
    c[n -  1] = 0
    alpha[0] = 0
    beta[0] = 0
    for i in range(0, n):  
        d = a[i] * alpha[i] + b[i]
        alpha [i + 1] = -c[i] / d
        
        beta [i + 1] = (f[i] - (a[i] * beta[i])) / (d)
    x[n - 1] = beta[n]
    print(alpha)
    print(beta)
    for i in range(n - 2, -1, -1):
        x[i] = int(alpha[i + 1] * x[i + 1] + beta[i + 1])
    x[n - 1] = round(x[n - 1])
    return x

#n = (int(input()))
a = [0, 1, 1]
b = [4, 3, 2]
c = [3, 1, 0]
f = [10, 10, 8]
A = np.array([[0, 1, 1], [4, 3, 2], [3, 1, 0]])
print(A)
print(a)
print(b)
print(c)
print(f)
print(sweep(a, b, c, f, 3))
print(solve_banded((1, 1), A, f))