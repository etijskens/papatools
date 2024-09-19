from mpi4py import MPI
import numpy as np

comm_world = MPI.COMM_WORLD
my_rank = comm_world.Get_rank()
num_procs = comm_world.Get_size()

# number of times to run the dice for all processes
n = 6400

my_results = np.random.randint(1,7,n//num_procs) # n/num_procs random number between 1 and 6

if my_rank == 0:
    # show our own results:
    print (f'process #{my_rank} obtained {my_results}')
    # reveive data from all processes but myself:
    for p in range (1, num_procs):
        p_results = comm_world.recv(source=p)
        # show results of process with rank p:
        print (f'process #{p} obtained {p_results}')
        # add the result of this process to my own results:
        my_results = np.concatenate((my_results, p_results))
    # Now show the global results we obtained in all processes:
    print (f"The global results are: {my_results}")
    # calculate the mean value
    print (f"The average of all data is {np.mean(my_results)}")
    # calculate the frequency distribution
    for i in range(1,7):
        fd = np.unique(my_results, return_counts=True)
    print (f"Frequency distribution: {fd}")
else:
    # send our results to the process with rank==0:
    comm_world.send(my_results, dest=0)
