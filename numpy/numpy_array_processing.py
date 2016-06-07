import numpy as np
import matplotlib.pyplot as plt

points = np.arange(-5, 5, 0.01)
dx, dy = np.meshgrid(points, points)
print 'dx'
print dx  # goes from -5 to +5 along x
print 'dy'
print dy  # goes from -5 to +5 along y
z = (np.sin(dx) + np.sin(dy))
print z
plt.imshow(z)
plt.colorbar()
plt.title("Plot for sin x + sin y")
# plt.show()

# numpy where
A = np.array([1, 2, 3, 4])
B = np.array([100, 200, 300, 400])
condition = np.array([True, True, False, False])
answer = [(A_val if cond else B_val)
          for A_val, B_val, cond in zip(A, B, condition)]
print answer
answer2 = np.where(condition, A, B)
print answer2

from numpy.random import randn
arr = randn(5,5)
print arr
print np.where(arr<0,0,arr)
print arr

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print arr.sum()
print arr.sum(0)

print arr.mean()
print arr.std()
print arr.var()

bool_arr = np.array([True,False,True])
print bool_arr.any()
print bool_arr.all()


#sort
arr=randn(5)
print arr
arr.sort()
print arr

countries =np.array(['France','Germany','USA','Russian','USA',"MEXICO","Germany"])
print np.unique(countries)

print np.in1d(['France','USA',"Sweden"],countries)
#if france usa and sweden are in countries
