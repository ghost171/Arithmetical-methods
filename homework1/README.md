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

## Examples:
### Hauss:

| INPUT    |My answer              |  Linalg    |
|----------|:---------------------:|-----------:|
| 5        |-0.1418285225780587    |-0.14182852257805872  |
|          |0.28631627795703035    |0.2863162779570304  |
|          |-0.1303044643745032    |-0.1303044643745032  |
|          |0.09585975915022188    |
0.09585975915022182 |
|          |0.4674462860378487     |0.46744628603784877   |
INPUT:5

OUTPUT:

LINALG

-0.1418285225780587

0.28631627795703035

-0.1303044643745032

0.09585975915022188

0.4674462860378487

MY SOLUTION

-0.14182852257805872

0.2863162779570304

-0.1303044643745032

0.09585975915022182

0.46744628603784877

MY TIME: 0.0005290508270263672

LINALG TIME 0.0004374980926513672

### Cholesky:

| INPUT    |      Linalg                                               |  My answer                            |
|----------|:---------------------------------------------------------:|--------------------------------------:|
| 5        | 1.48631135  0.          0.          0.          0.        |1.4863113522472047, 0.0, 0.0, 0.0, 0.0                                                               |
|          | 1.47610002  1.31677216  0.          0.          0.        |1.4761000184104431, 1.3167721587989418, 0.0, 0.0, 0.0                                                      |
|          | 1.11244962 -0.01951318  1.57392964  0.          0.        |1.1124496222065503, -0.019513182251388754, 1.5739296399484872, 0.0, 0.0                                    |
|          | 0.23199587 -0.02030996  0.49457816  0.44926542  0.        |0.23199586777156372, -0.02030996355810667, 0.49457815868579463, 0.44926542177867457, 0.0                   |
|          | 0.36217338  1.08403672  0.17329777 -0.02367541  1.00511403|0.362173377785772, 1.0840367222629377, 0.1732977718832061, -0.023675406081248573, 1.0051140332087618   |
#### INPUT:

5

#### OUTPUT:

A:

[[1.2351388  0.68377145 0.45958868 0.06551911 0.02226377]
 
 [0.68377145 1.71878489 0.34239625 0.04894144 0.6093971 ]
 
 [0.45958868 0.34239625 1.78679321 0.41987781 0.13339847]
 
 [0.06551911 0.04894144 0.41987781 0.56307395 0.02537487]
 
 [0.02226377 0.6093971  0.13339847 0.02537487 1.39887544]]

Linalg:

[[ 1.48631135  0.          0.          0.          0.        ]
 
 [ 1.47610002  1.31677216  0.          0.          0.        ]
 
 [ 1.11244962 -0.01951318  1.57392964  0.          0.        ]
 
 [ 0.23199587 -0.02030996  0.49457816  0.44926542  0.        ]
 
 [ 0.36217338  1.08403672  0.17329777 -0.02367541  1.00511403]]

L(Answer):

[[1.4863113522472047, 0.0, 0.0, 0.0, 0.0], 

[1.4761000184104431, 1.3167721587989418, 0.0, 0.0, 0.0], 

[1.1124496222065503, -0.019513182251388754, 1.5739296399484872, 0.0, 0.0], 

[0.23199586777156372, -0.02030996355810667, 0.49457815868579463, 0.44926542177867457, 0.0], 

[0.362173377785772, 1.0840367222629377, 0.1732977718832061, -0.023675406081248573, 1.0051140332087618]]

MY TIME: 0.00018310546875

LINALG TIME: 0.001438140869140625

### Sweep:
| INPUT    |My answer      |  Linalg    |
|----------|:-------------:|-----------:|
| 5        |  1.75898992   |1.75898992  |
|          |  0.27559671   |0.27559671  |
|          | 0.01612521    |0.01612521  |
|          | 0.44045912    | 0.44045912 |
|          | 0.9301341     |0.9301341   |
#### INPUT:

5

#### OUTPUT:

My alg: [1.75898992 0.27559671 0.01612521 0.44045912 0.9301341 ]

Linalg: [1.75898992 0.27559671 0.01612521 0.44045912 0.9301341 ]

My time: 0.00043892860412597656

Linalg time: 0.02393507957458496


## Illustrations of graphics

### Hauss
![alt text](https://github.com/ghost171/Arithmetical-methods/blob/master/homework1/Hauss.png)

### Cholesky
![alt text](https://github.com/ghost171/Arithmetical-methods/blob/master/homework1/Cholesky.png)

### Sweep
![alt text](https://github.com/ghost171/Arithmetical-methods/blob/master/homework1/sweep.png)
