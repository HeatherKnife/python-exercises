import numpy as np
#a
a = np.zeros(10)
a[4]=1
print(a)

#b
v = np.arange(10,49,1)
print(v)

#c
v_reverse = v[::-1]
print(v_reverse)

#d
m = np.arange(9).reshape(3,3)
print(m)

#e
vector = [1,2,0,0,4,0]
x=np.nonzero(vector)
print(x)

#f
vector_rand = np.random.rand(30)
print(np.mean(vector_rand))

#g
matrix = np.zeros((4,4))
matrix[0, :] = 1
matrix[-1,:] = 1
matrix[:, 0] = 1
matrix[:,-1] = 1
print(matrix)

#h
matrix_pattern_0 = np.zeros((8,8))
matrix_pattern_0[1::2,::2] = 1
matrix_pattern_0[::2,1::2] = 1
print(matrix_pattern_0)

#i
matrix_pattern_1 = np.tile([["0", "*"], ["*", "0"]], (4, 4))
print(matrix_pattern_1)

#j
Z = np.arange(11)
m = (Z > 3) & ( Z < 8 )
Z[m] *= -1
print(Z)

#k
Z1 = np.random.random(10)
Z1 = np.sort(Z1)
print(Z1)

#l
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
print(A)
print(B)
equal = np.equal(A,B)
print(equal)

#m
Z = np.arange(10, dtype=np.int32)
print(Z.dtype)
Z = np.arange(10, dtype=np.float32)
print(Z.dtype)

#n
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
D = np.diag(C)
print(C)
print(D)

