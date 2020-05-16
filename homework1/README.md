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

## Explain the programs
### Hauss
Gaussian elimination, also known as row reduction, is an algorithm in linear algebra for solving a system of linear equations.
It is usually understood as a sequence of operations performed on the corresponding matrix of coefficients.
Row operations
See also: Elementary matrix
There are three types of elementary row operations which may be performed on the rows of a matrix:

Swap the positions of two rows.
Multiply a row by a non-zero scalar.
Add to one row a scalar multiple of another.

If the matrix is associated to a system of linear equations, then these operations do not change the solution set. 
Therefore, if one's goal is to solve a system of linear equations, then using these row operations could make the problem easier. 
Also, that program generates random matrix for our terms. 
    
 ### Sweep 
 In numerical linear algebra, the tridiagonal matrix algorithm, also known as the Thomas algorithm (named after Llewellyn Thomas), is a simplified form of Gaussian elimination that can be used to solve tridiagonal systems of equations.
Or such systems, the solution can be obtained in O(n) operations instead of O(n^3) required by Gaussian elimination. 
And then an (abbreviated) backward substitution produces the solution. Examples of such matrices commonly arise from the discretization of 1D Poisson equation and natural cubic spline interpolation. 
Also, that program generates random matrix for our terms. 

### Cholseky
In linear algebra, the Cholesky decomposition or Cholesky factorization (pronounced /ʃo-LESS-key/) is a decomposition of a Hermitian, positive-definite matrix into the product of a lower triangular matrix and its conjugate transpose.
A closely related variant of the classical Cholesky decomposition is the LDL decomposition,

    A = LDL*
where L is a lower unit triangular (unitriangular) matrix, and D is a diagonal matrix.

This decomposition is related to the classical Cholesky decomposition of the form LL* as follows: 
    
    A=LDL* =LD^(1/2)D*^(1/2)L*^(1/2) = (LD^(1/2)) (LD^(1/2))*
    
 The LDL variant, if efficiently implemented, requires the same space and computational complexity to construct and use but avoids extracting square roots. 
 Some indefinite matrices for which no Cholesky decomposition exists have an LDL decomposition with negative entries in D.
 For these reasons, the LDL decomposition may be preferred. For real matrices, the factorization has the form A = LDLT and is often referred to as LDLT decomposition (or LDLT decomposition, or LDL′). 
 It is closely related to the eigendecomposition of real symmetric matrices, A = QΛQT. 
 Also, that program generates random matrix for our terms. 
 

## Input

Because that program generates current matrix that program receives sizes of matrix. 

## Time graphics

Times-graphic was builded. This is dependency time of our program's work from size of our matrix. There are:

Hauss.png 
Cholesky.png 
Sweep.png
