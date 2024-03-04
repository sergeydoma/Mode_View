# share numpy array via pipe
from multiprocessing import Process
from multiprocessing import Pipe

import numpy as np
from numpy import ones


# task executed in a child process
def task(pipe):
	# define the size of the numpy array
	n = 10000
	# create the numpy array
	# data = ones((n, n))
	array = ones((n, n))
	# check some data in the array
	array[1][1] = 555
	print ( array[:5, :5] )
	# send the array via a pipe
	pipe.send (array)


# protect the entry point
if 1 == 1:
	# create the shared pipe
	conn1, conn2 = Pipe ()
	# create a child process
	child = Process ( target=task, args=(conn2,) )
	# start the child process
	child.start ()
	# read the data from the pipe
	np.array = conn1.recv ()
	# check some data in the array
	print(np.array[:5, :5] )