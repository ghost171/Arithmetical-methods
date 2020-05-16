# This version for separate folds
## How to execute a program?

1) From python3 

You have to write "python3 " + the number of the program that you want to check.
For example:

    python3 Hauss.py 

2) Jupyter

You have to write "jupyter notebook " and of the homework that you want to check.
Secondly, you must add ".ipynb" to the note.
For example:
  
    jupyter notebook homework1.ipynb

To execute the programs in Jupyter press button-combination Shift+Enter.

## What do this programs.

### Jacobi
 In numerical linear algebra, the Jacobi method is an iterative algorithm for determining the solutions of a strictly diagonally dominant system of linear equations. 
 Each diagonal element is solved for, and an approximate value is plugged in. The process is then iterated until it converges.
 This algorithm is a stripped-down version of the Jacobi transformation method of matrix diagonalization. 
 The method is named after Carl Gustav Jacob Jacobi.
 
    sum{1, n} is a row from 1 to n.
    sum{1, n}(a[i][j] * x[j]) = b[i]
 solve for the value of x_i while assuming the other entries of x remain fixed. This gives 
    
    x[i](k) = ((b[i] - sum{i != j}(a[i][j] * x[j](k - 1))) / a[i][i])
 which is the Jacobi method.
 In this method, the order in which the equations are examined is irrelevant, since the Jacobi method treats them independently. The definition of the Jacobi method can be expressed with matrices as 
    
    x(k) = D^(-1)(L + U)x^(k - 1) + D^(-1)b
 where the matrices D, -L, and -U represent thediagonal, strictly lower triangular, and strictly upper triangular parts of A, respectively. 
 Also, that program generates random matrix for our terms. 
 ### Seidel
 In numerical linear algebra, the Gauss–Seidel method, also known as the Liebmann method or the method of successive displacement, is an iterative method used to solve a linear system of equations. 
 It is named after the German mathematicians Carl Friedrich Gauss and Philipp Ludwig von Seidel, and is similar to the Jacobi method. 
 Though it can be applied to any matrix with non-zero elements on the diagonals, convergence is only guaranteed if the matrix is either diagonally dominant, or symmetric and positive definite. 
 It was only mentioned in a private letter from Gauss to his student Gerling in 1823. A publication was not delivered before 1874 by Seidel. 
 The Gauss–Seidel method is an iterative technique for solving a square system of n linear equations with unknown x: 
 
    sum{1, n} is a row from 1 to n.
    Ax = b
 This is defined the operation:
    
    L*x(k + 1) = b - Ux(k)
 
 Where x(k)  is the kth approximation or iteration of x, x(k+1)  is the next or k + 1 iteration of x , and the matrix A is decomposed into a lower triangular component L* and a strictly upper triangular component U: 
    
    A = L∗(U).
 The system of linear equations may be rewritten as: 
    
    (L*)x = b - Ux
 The Gauss–Seidel method now solves the left hand side of this expression for x, using previous value for x on the right hand side. 
 Analytically, this may be written as: 
    
    x(k + 1) = (L*)^(-1)(b - Ux(k))
Also, that program generates random matrix for our terms. 

## Input data
 As input, programs receive matrix sizes.
## Time graphics
Times-graphic was builded. This is  dependency time of our program's work from size of our matrix.
There are:
 
 Hauss.png
 Cholesky.png
 Sweep.png
 
