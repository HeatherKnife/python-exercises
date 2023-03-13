# Program to multiply two matrices using nested loops
import random
import numpy as np

N = 250

X = np.random.randint(0,100, size=(N,N))
Y = np.random.randint(0,100, size=(N,N+1))

result = np.dot(X,Y)

for r in result:
    print(r)

