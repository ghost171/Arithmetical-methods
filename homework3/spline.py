import string
import numpy as np
from scipy import interpolate

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
    for i in range(n - 2, -1, -1):
        x[i] = alpha[i + 1] * x[i + 1] + beta[i + 1]
    return x

def generateSpline (x , y):
    n = x.shape[0] - 1
    h = ( x[ n ] - x[0]) / n
    a = np.array ([0] + [1] * ( n - 1) + [0])
    b = np.array ([1] + [4] * ( n - 1) + [1])
    c = np.array ([0] + [1] * ( n - 1) + [0])

    f = np.zeros (n + 1)
    for i in range (1 , n):
        f[ i ] = 3 * ( y [i -1] - 2 * y[i ] + y[i + 1]) / h**2
    s = sweep( a , b , c , f, n + 1)
    B = [0] * (n + 1)   
    A = [0] * (n + 1)
    C = [0] * (n + 1)
    D = [0] * (n + 1)
    for i in range (n):
        B [ i ] = s [ i ]
        D [ i ] = y [ i ]
    for i in range(n):
        A[i] = (B[i + 1] - B[i]) / (3 * h)
        C[i] = ((y[i + 1] - y[i]) / h) - ((B[i + 1] + 2 * B[i]) * h) / 3
    return A , B , C , D

handle = open("train.dat")
data = handle.read()
x = []
for i in range(len(data)):
    if(data[i].isdigit() == True):
        x.append(int(data[i]))
handle.close()
handle = open("train.ans")
data = handle.read()
y = []
for i in range(len(data)):
    if data[i].isdigit() == True:
        y.append(int(data[i]))
handle.close()
x = np.array(x)
y = np.array(y)
A, B ,C , D = generateSpline(x, y)
handle = open('test.ans', 'w')
for el in A:
    handle.write(str(el) + " ")
handle.write("\n")
for el in B:
    handle.write(str(el) + " ")
handle.write("\n")
for el in C:
    handle.write(str(el) + " ")
handle.write("\n")
for el in D:
    handle.write(str(el) + " ")
handle.write("\n")
handle.close()

print(A)
print(B)
print(C)
print(D)    