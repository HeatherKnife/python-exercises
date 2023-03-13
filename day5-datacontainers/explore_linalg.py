import numpy as np
import random
# from numpy.linalg import multi_dot, inv
from scipy import linalg
import scipy
from scipy.stats import poisson
from scipy.stats import norm
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

#a
A = np.array([[1, 2, 3],
 			  [4, 6, 6],
 			  [7, 8, 9]])

#b
v=np.array([1, 2, 3])


# sol = np.linalg.det(A)
#c
sol = np.dot(np.linalg.inv(A),v)
print(sol)
#d
print(np.dot(A,sol))

#e
R = np.array(np.random.rand(9)).reshape(3,3)
sol2 = np.dot(np.linalg.inv(R),v)
print(sol2)
print(np.dot(R,sol2))

#f
EigenVal, EigenVec = linalg.eig(A)
print("Eigen Val", EigenVal)
print("Eigen Vec", EigenVec)

print(A@EigenVec[:,0]-EigenVal[0]*EigenVec[:,0])

#g
print(np.linalg.det(np.linalg.inv(A)))

#h
print(np.linalg.norm(A))
print(np.linalg.norm(A, ord=2))
print(np.linalg.norm(A, 'fro'))
print(np.linalg.norm(A, np.inf))

#Statistics

#a
#PMF
plt.plot(np.linspace(0,10,1000), poisson.pmf(np.linspace(0,10,1000), mu=0.7))
plt.xlabel('bins')
plt.ylabel('Poisson Probability Mass Function')
plt.show()

#cumulative distribution
plt.plot(np.linspace(0,10,1000), poisson.cdf(np.linspace(0,10,1000), mu=0.7))
plt.xlabel('bins')
plt.ylabel('Cumulative Poisson')
plt.show()

#Histogram
#rvs -> "Random State Variable"
samples_poisson = poisson.rvs(mu = 0.5, size=1000)
# print("max samples_poisson",np.max(samples_poisson))
plt.hist(samples_poisson, bins = np.arange(0,10))
plt.xlabel('bins')
plt.ylabel('Counts Poisson')
plt.show()

#b 
#PMF ----> It doesn't exist a PMF since it is a continous distribution 
plt.plot(np.linspace(-10,10,1000), norm.pdf(np.linspace(-10,10,1000)))
plt.xlabel('bins')
plt.ylabel('Normal Probability Mass Function')
plt.show()

#cumulative distribution
plt.plot(np.linspace(0,10,1000), norm.cdf(np.linspace(0,10,1000)))
plt.xlabel('bins')
plt.ylabel('Cumulative Normal')
plt.show()

#Histogram
#rvs -> "Random State Variable"
samples_normal = norm.rvs(size=1000)
plt.hist(samples_normal, bins = np.arange(-10,10))
plt.xlabel('bins')
plt.ylabel('Counts Poisson')
plt.show()

#c
t_stat, p_value = ttest_ind(samples_poisson, samples_normal)
print("t_stat", t_stat)
print("p_value", p_value)
if (p_value < 0.05): 
	print("Data from two different dists")