import numpy as np 
arr = np.arange(5)
np.save("myarray",arr)
arr =np.arange(10)
print np.load('myarray.npy')
arr1= np.load('myarray.npy')
arr2 = arr
np.savez('ziparray.npz',x=arr1,y=arr2)
archive=np.load('ziparray.npz')
print archive['x']
print archive['y']

arr = np.array([[1,2,3],[4,5,6]])

np.savetxt('mytextarray.txt',arr,delimiter=',')

arr= np.loadtxt('mytextarray.txt',delimiter=',')
print arr