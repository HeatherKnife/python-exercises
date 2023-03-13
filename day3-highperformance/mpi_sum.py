from mpi4py import MPI
import numpy as np

commmunicator = MPI.COMM_WORLD
rank = commmunicator.Get_rank()
size = commmunicator.Get_size()

data = np.random.rand(10)

sum_data = np.zeros(1)
commmunicator.Reduce(np.sum(data), sum_data, op=MPI.SUM, root=0)

if rank == 0:
    print(sum_data[0])


#Failed attempt

# from mpi4py import MPI
# import numpy as np

# communicator = MPI.COMM_WORLD
# rank = communicator.Get_rank()

# #generate this matrix per process
# Z = np.zeros(1)

# #gather the processes
# numbers = communicator.gather(Z, root=0)

# #sum the processes
# if rank == 0:
#   if numbers is not None:
#       total = communicator.reduce(sum(numbers), op=MPI.SUM)
#       print("total") 
#       print(total)
# else:
#   communicator.send(Z, dest = 0)