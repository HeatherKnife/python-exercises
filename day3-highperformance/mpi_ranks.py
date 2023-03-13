from mpi4py import MPI

communicator = MPI.COMM_WORLD
rank = communicator.Get_rank()

print(rank)

# I got this output
# mpirun -n 4 python mpi_ranks.py
# 1
# 3
# 0
# 2
