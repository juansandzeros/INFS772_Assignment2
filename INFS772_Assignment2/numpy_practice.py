__author__ = 'Juan Harrington' # please type your name

import numpy as np

def main():
    #1. Create a numpy array that includes evenly spaced numbers over an interval from 1.3(inclusive) to 2.5(exclusive). This array should include 61 numbers.
    ''' Your code here...'''
    a = np.linspace(1.3,2.5,num=61,endpoint=False)
    print a
    ''' your code should print:
    [ 1.3         1.31967213  1.33934426  1.35901639  1.37868852  1.39836066
  1.41803279  1.43770492  1.45737705  1.47704918  1.49672131  1.51639344
  1.53606557  1.5557377   1.57540984  1.59508197  1.6147541   1.63442623
  1.65409836  1.67377049  1.69344262  1.71311475  1.73278689  1.75245902
  1.77213115  1.79180328  1.81147541  1.83114754  1.85081967  1.8704918
  1.89016393  1.90983607  1.9295082   1.94918033  1.96885246  1.98852459
  2.00819672  2.02786885  2.04754098  2.06721311  2.08688525  2.10655738
  2.12622951  2.14590164  2.16557377  2.1852459   2.20491803  2.22459016
  2.2442623   2.26393443  2.28360656  2.30327869  2.32295082  2.34262295
  2.36229508  2.38196721  2.40163934  2.42131148  2.44098361  2.46065574
  2.48032787]
  '''
    #2.	Create a numpy array of the first 10 odd integers (including 1,3,5,7,9,11,13,15,17,19). You need to use arange() function.
    #''' your code here...'''
    b = np.arange(1,20,step=2)
    print b
    ''' Your code should print:
    [ 1  3  5  7  9 11 13 15 17 19]
    '''
    # 3. create a 10*10 numpy arrays of zeros and then frame it with a border of ones. Please do not use numpy.array() to directly create such a 2d array
    # You need to use method such as numpy.zero(), numpy.row_stack(), etc.
    c = np.zeros((10,10))
    print c
    ''' your code here...
    Your code should print:
    [[ 1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.]
 [ 1.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  1.]
 [ 1.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  1.]
 [ 1.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  1.]
 [ 1.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  1.]
 [ 1.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  1.]
 [ 1.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  1.]
 [ 1.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  1.]
 [ 1.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  1.]
 [ 1.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  1.]
 [ 1.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  1.]
 [ 1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.]]
    '''
    # 4.Create a random 3x5 array using the np.random.rand(3, 5) function and then compute: the sum of all the entries, the sum of the rows and the sum of the columns. (Note: you need to use axis= argument!)
    ''' your code here...
    4.1 your code for printing the sum of all elements;
    4.2 your code for printing the sum of rows
    4.3 your code for printing the sum of columns.
    '''
    r = np.random.rand(3,5)
    print r
    print np.sum(r)
    print np.sum(r,axis=0) #columns
    print np.sum(r,axis=1) #rows

if __name__ == '__main__':
    main()