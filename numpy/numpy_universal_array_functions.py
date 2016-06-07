# deals with all the different functions that apply to arrays.
import numpy as np 
arr= np.arange(11)
print arr

#Unary Functions
print np.sqrt(arr)
#e to the power
print np.exp(arr)

#Binary Functions

A=np.random.randn(10)
print A
B= np.random.randn(10)
print B

print np.add(A,B)

# get maximum values for each entry and build an array
print np.maximum(A,B)
print np.minimum(A,B)