import numpy as np
import math
n = 4
def seidel (A , f , x ):
    xnew = [0] * n
    for i in range(0, n - 1):
        s = 0
        for j in range(0, i - 1):
            s = s + A [ i ][ j ] * xnew [ j ]
        for j in range(i + 1, n - 1):
            s = s + A[ i ][ j ] * x[ j ]
        xnew[ i ] = int(( f[ i ] - s) / A [ i ][ i ])
    return xnew

def diff(x, xnew):
    s = 0
    for i in range(0, n - 1):
        s += (x[i] - xnew[i]) * (x[i] - xnew[i])
    return int(math.sqrt(s))

def solve (A , f ):
    xnew = n * [0]
    eps = 0.2
    while True:
        x = xnew
        xnew = seidel (A , f , x )
        if(diff(x, xnew) <= eps):
            print(x)
            break

A = np.array(   [
                [2, -1, 0, -1],
                [0, 2, -1, 0],
                [-1, 1, 3, 0],
                [1, 0, -2, 4]
                ])
f = np.array([4, 3, 2, 1])
solve(A, f)