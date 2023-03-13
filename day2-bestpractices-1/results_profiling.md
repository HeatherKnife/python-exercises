# Profiling multmat.py

# Before Profiling

Wrote profile results to matmult.py.lprof
Timer unit: 1e-06 s

Total time: 8.81994 s
File: matmult.py
Function: mat_mult at line 6

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     6                                           @profile
     7                                           def mat_mult():
     8                                               # NxN matrix
     9         1          0.5      0.5      0.0      X = []
    10       250         36.8      0.1      0.0      for i in range(N):
    11       250     128866.4    515.5      1.5          X.append([random.randint(0,100) for r in range(N)])
    12                                           
    13                                               # Nx(N+1) matrix
    14         1          0.2      0.2      0.0      Y = []
    15       250         36.3      0.1      0.0      for i in range(N):
    16       250     129297.7    517.2      1.5          Y.append([random.randint(0,100) for r in range(N+1)])
    17                                           
    18                                               # result is Nx(N+1)
    19         1          0.2      0.2      0.0      result = []
    20       250         34.8      0.1      0.0      for i in range(N):
    21       250        638.1      2.6      0.0          result.append([0] * (N+1))
    22                                           
    23                                               # iterate through rows of X
    24       250         33.5      0.1      0.0      for i in range(len(X)):
    25                                                   # iterate through columns of Y
    26     62750       8369.9      0.1      0.1          for j in range(len(Y[0])):
    27                                                       # iterate through rows of Y
    28  15687500    2071488.0      0.1     23.5              for k in range(len(Y)):
    29  15687500    6461788.8      0.4     73.3                  result[i][j] += X[i][k] * Y[k][j]
    30                                           
    31       250         52.9      0.2      0.0      for r in result:
    32       250      19296.4     77.2      0.2          print(r)


# After profiling

Wrote profile results to matmult.py.lprof
Timer unit: 1e-06 s

Total time: 8.86059 s
File: matmult.py
Function: mat_mult at line 6

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     6                                           @profile
     7                                           def mat_mult():
     8                                               # NxN matrix
     9                                               # X = []
    10                                               # for i in range(N):
    11                                                   #X.append([random.randint(0,100) for r in range(N)])
    12         1     129382.4 129382.4      1.5      X = [[random.randint(0,100) for r in range(N)] for i in range(N)]
    13                                           
    14                                               # Nx(N+1) matrix
    15                                               # Y = []
    16                                               # for i in range(N):
    17                                                   #Y.append([random.randint(0,100) for r in range(N+1)])
    18         1     128643.4 128643.4      1.5      Y = [[random.randint(0,100) for r in range(N+1)] for i in range(N)]
    19                                           
    20                                               # result is Nx(N+1)
    21                                               # result = []
    22                                               # for i in range(N):
    23                                                   #result.append([0] * (N+1))
    24         1        257.2    257.2      0.0      result = [[0] * (N+1) for i in range(N)]
    25                                           
    26                                               # iterate through rows of X
    27       250         31.0      0.1      0.0      for i in range(len(X)):
    28                                                   # iterate through columns of Y
    29     62750       8211.0      0.1      0.1          for j in range(len(Y[0])):
    30                                                       # iterate through rows of Y
    31  15687500    2140875.4      0.1     24.2              for k in range(len(Y)):
    32  15687500    6431994.8      0.4     72.6                  result[i][j] += X[i][k] * Y[k][j]
    33                                           
    34       250         49.1      0.2      0.0      for r in result:
    35       250      21145.7     84.6      0.2          print(r)

# Profiling euler72.py

Wrote profile results to euler72.py.lprof
Timer unit: 1e-06 s

Total time: 0.00246152 s
File: euler72.py
Function: gen_primes at line 4

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     4                                           @profile
     5                                           def gen_primes(n):
     6         1          1.1      1.1      0.0      l = range(2,n)
     7         1          0.2      0.2      0.0      primes = []
     8       998        162.9      0.2      6.6      for j in range(0,len(l)):
     9       998        124.0      0.1      5.0          p = True
    10      2967        428.5      0.1     17.4          for d in primes:
    11      2800        788.4      0.3     32.0              if(d > sqrt(l[j])):
    12       167         24.9      0.1      1.0                  break
    13      1970        513.9      0.3     20.9              if(l[j] % d == 0):
    14       830        101.1      0.1      4.1                  p = False
    15       830        114.8      0.1      4.7                  break;
    16       830        148.5      0.2      6.0          if(p):
    17       168         53.0      0.3      2.2              primes.append(l[j])
    18                                           
    19         1          0.2      0.2      0.0      return primes

Total time: 0.0787505 s
File: euler72.py
Function: factorize at line 21

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    21                                           @profile
    22                                           def factorize(n,primes):
    23      9999       1457.8      0.1      1.9      factors = []
    24      9999       1401.1      0.1      1.8      init_n = n
    25     96347      15198.4      0.2     19.3      for p in primes:
    26     96347      22674.3      0.2     28.8          while(n%p == 0):
    27     22389       3941.7      0.2      5.0              n = n/p
    28     22389       4839.0      0.2      6.1              factors.append(p)
    29     86348      22250.5      0.3     28.3          if(p > sqrt(n)):
    30      9999       1378.6      0.1      1.8              break
    31      9596       1795.1      0.2      2.3      if(n > 1):
    32      9596       2223.0      0.2      2.8          factors.append(n)
    33      9999       1591.0      0.2      2.0      return factors

Total time: 0.217673 s
File: euler72.py
Function: fast_phi at line 50

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    50                                           @profile
    51                                           def fast_phi(n,primes):
    52      9999     196528.3     19.7     90.3      factors = factorize(n,primes)
    53      9999       2366.0      0.2      1.1      phi = factors[0]-1
    54     21986       6160.0      0.3      2.8      for i in range(1,len(factors)):
    55     14301       4117.6      0.3      1.9          if(factors[i] == factors[i-1]):
    56      7685       3219.9      0.4      1.5              phi *= (factors[i]-1)*(factors[i])/(factors[i]-1)
    57                                                   else:
    58     14301       3881.9      0.3      1.8              phi *= (factors[i]-1)
    59      9999       1399.1      0.1      0.6      return phi


I would start optimizing the script by changing the append method to fill the 
arrays.