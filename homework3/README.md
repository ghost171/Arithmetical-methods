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

## Hint for understaing:
This program take input data from files. So, user can't excute it from the main directory of the repository.

Lets note what programs use:
  
  linear_interpolation: train1.dat, train1.ans, test1.dat, test1.ans
  
  Lagrange_interpolate: train2.dat, train2.ans, test2.dat, test2.ans
  
  spline: train.dat, train.ans, test.dat, test.ans
  
 If you going to change input data, write your changes in the files train.dat, train.ans, test.dat.
 In test.ans you have an answer

## How does this programs works?
### Linear interpolation
If the two known points are given by the coordinates.
the linear interpolant is the straight line between these points. For a value x in the interval ( x0 , x1 ) the value y along the straight line is given from the equation of slopes (y - y0)/
