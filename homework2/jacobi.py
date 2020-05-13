import numpy as np
import math
n = 4
def jacobi (A , f , x ):
    xnew = n * [0]
    for i in range(n):
        s = 0
        for j in range(0, i):
            s = s + A [ i ][ j ] * x [ j ]
        for j in range(i + 1, n):
            s = s + A [ i ][ j ] * x [ j ]
        xnew[ i ] = ( f [ i ] - s ) / A [ i ][ i ]
    return xnew

def diff(x, xnew):
    s = float(0)
    for i in range(n):
        s += float((x[i] - xnew[i]) ** 2) 
    return float(math.sqrt(s))

def solve (A , f):
    eps = 0.2
    xnew = n * [0]
    while True:
        x = xnew
        xnew = jacobi (A , f , x )
        if ( abs(diff(x, xnew )) < abs(eps) ):
            print(x)
            for i in range(n):
                x[i] = round(x[i])
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