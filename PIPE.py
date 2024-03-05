# share numpy array via pipe
from multiprocessing import Process
from multiprocessing import Pipe
from numpy import ones
import numpy as np

class ArrayHelper ():
	def __init__(self, dim):
		self.array = np.ones(dim)

	# access array data by slice
	def getdata(self, array_slice):
		return self.array[array_slice]

	def setdata(self, array_slice, value):
		self.array[array_slice] = value
	def setOnedata(self, row, col, value):
		self.array[row][col] = value

	# call functions on the numpy array
	def sum(self):
		return self.array.sum ()

# task executed in a child process
def task(pipe):
	# define the size of the numpy array
	n = 10000
	# create the numpy array
	data = ones ((n, n))
	# check some data in the array
	print ('tack = ', data[:10, :10] )
	# send the array via a pipe
	pipe.send ( data )


# protect the entry point
if __name__ == '__main__':
	# create the shared pipe
	conn1, conn2 = Pipe ()
	# create a child process
	child = Process ( target=task, args=(conn2,))
	# start the child process
	child.start ()
	# read the data from the pipe
	data = conn1.recv ()
	# check some data in the array
	print ( 'Out =', data[:10, :10] )