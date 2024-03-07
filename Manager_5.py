from multiprocessing import Process
from multiprocessing.sharedctypes import RawArray

import numpy as np
from numpy import frombuffer
from numpy import double, ubyte


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
def task(array):
    # create a new numpy array backed by the raw array
    data = frombuffer(array, dtype=ubyte, count=len(array))

    # check the contents
    print(f'Child {data[:10]}')
    # increment the data
    data[:] += 1

    # data[2][2] = '555'
    # confirm change
    print(f'Child {data[:10]}')


# protect the entry point
if __name__ == '__main__':
    # define the size of the numpy array
    n = 1000 #0000
    # create the shared array
    array = RawArray('u', n)
    # create a new numpy array backed by the raw array
    data = frombuffer(array, dtype=ubyte, count=len(array))
    # populate the array
    data.fill(1.0)
    # confirm contents of the new array
    print('DATA!',data[:10], len(data))
    # create a child process
    child = Process(target=task, args=(array,))
    # start the child process
    child.start()
    # wait for the child process to complete
    child.join()
    # check some data in the shared array
    print('Data2',data[:10])