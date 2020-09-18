#1
import numpy as np

#2
print np.__version__
print np.show_config()

#3
x=np.zeros(10)
print x

#4
n = np.zeros((4,4))
print ("%d bytes" % (n.size * n.itemsize))

#5

n1 =np.zeros(10)
print n1
print ("update fifth value of the vector to 1")
n1[5]=1
print n1

#6
vector =np.arange(10,30)
print vector

#7
vector1 = vector[::-1]
print vector1

#8

matrix = np.arange(0,9).reshape(3,3)
print matrix

#9
matrix1 = np.identity(3)
print  matrix1

#10

array1 = np.random.random((3,3,3))
print array1

#11
array2 = np.random.random((10,10))
print array2
print "Minimum value"
array2min =array2.min()
print array2min
print "Maximum value"
array2max = array2.max()
print array2max

#12

vectorX = np.random.random(30)
print vectorX
print "Mean value"
vectorXmean = vectorX.mean()
print  vectorXmean

#13
array2d =np.ones((5,5))
print array2d
print "1 on the border and 0 inside "
array2d[1:-1,1:-1] = 0
print array2d

#14
print "existing array"
print matrix
print "0 on the border"
matrix = np.pad(matrix,pad_width=1,mode='constant')
print matrix

#15
matrixD = np.diag([1,2,3,4,])
print  matrixD

#16

matrixN = np.random.random((5,5))
print  matrixN
print "Normalization"
matrixNmax, matrixNmin = matrixN.max(), matrixN.min()
matrixN = (matrixN - matrixNmin)/(matrixNmax - matrixNmin)
print  matrixN



