import numpy as np
import time
import matplotlib.pyplot as plt

n = int(input())
A = np.random.rand(n, n)
f = np.random.rand(n)
A1 = A.copy()
f1 = f.copy()
for i in range(n):
    for j in range(n):
        if i != j:
            A[i][i] += A[i][j] 

linalg_time = time.time()
print()
print("LINALG")
print()
x1 = np.linalg.solve(A,f)
linalg_time = time.time() - linalg_time
for i in range(n):
    print(x1[i]),

print(linalg_time)
my_time = time.time()
for k in range(n):
        A[k, k + 1:] = A[k, k + 1:] / A[k, k]
        f[k] /= A[k][k]    
        for i in range(k + 1, n):
            A[i, k + 1:] -= A[i][k] * A[k, k + 1:]
            f[i] -= A[i][k] * f[k]
        A[k + 1:, k] = np.zeros(n - k - 1)
x = np.zeros(n)
for i in range(n - 1, -1, -1):
    x[i] = f[i]
    for j in range(i + 1, n):
        x[i] -= A[i][j] * x[j]
my_time = time.time() - my_time
print()
print("MY SOLUTION")
print()
for i in range(n):
    print(x[i])
print()
print("MY TIME:", my_time)
print("LINALG TIME", linalg_time)
