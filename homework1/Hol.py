#Cholesky method
import math
import numpy as np
import time

def cholesky(A):
    n = len(A)
    L = [[0.0] * n for i in range(n)]
    for i in range(n):
        for k in range(i + 1):
            tmp_sum = sum(L[i][j] * L[k][j] for j in range(k))
            if (i == k): 
                L[i][k] = math.sqrt(abs(A[i][i] - tmp_sum))
            else:
                L[i][k] = (1.0 / L[k][k] * (A[i][k] - tmp_sum))
    return L
n = 3
X = np.random.rand(n, n)
A = np.transpose(X) * X

for i in range(n):
    for j in range(n):
        if i != j:
            A[i][i] += A[i][j] 

L = A

L = A.dot(np.transpose(L))


my_time = time.time()
B = cholesky(L)
my_time = time.time() - my_time

print ("A:")
print(A)

print("Linalg:")
linalg_time = time.time()
print(np.linalg.cholesky(L))
linalg_time = time.time() - linalg_time

print ("L(Answer):")
print(B)

print("MY TIME:", my_time)
print("LINALG TIME:", linalg_time)