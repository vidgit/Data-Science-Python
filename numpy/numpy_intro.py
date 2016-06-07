import numpy as np
# creating arrays

# 1D Array
my_list1 = [1, 2, 3, 4]
my_array1 = np.array(my_list1)
print type(my_array1), my_array1

# 2D Array
my_list2 = [11, 22, 33, 44]
my_lists = [my_list1, my_list2]
my_array2 = np.array(my_lists)

print type(my_array2), my_array2
print "Shape", my_array2.shape
print my_array2.dtype

# Special Arrays
my_zeros = np.zeros(5)
print my_zeros, my_zeros.dtype

my_ones = np.ones([5, 5])
print my_ones
print np.empty(5)

print np.eye(5)
# (start, stop, stepsize)
print np.arange(5)
print np.arange(5, 50, 2)