# share a numpy array between processes using a manager
from multiprocessing import Process
from multiprocessing.managers import BaseManager
from numpy import ones
import numpy as np



# custom manager to support custom classes
class CustomManager ( BaseManager ):
	# nothing
	pass

	def ArrayHelper(self, param):
		pass


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
def task(data_proxy):
	for i in range(1):
	# report details of the array
		print ( f'Array sum (in child): {data_proxy.sum ()}' )
		data_proxy.setOnedata(1,3, 803)
		print ( 'Tack',data_proxy.getdata ( slice ( 0, 10 ) ) )

# protect the entry point
if __name__ == '__main__':
	# register the a python class with the custom manager
	CustomManager.register ( 'ArrayHelper', ArrayHelper )
	# create and start the custom manager
	with CustomManager () as manager:
		# define the size of the numpy array
		# n = 100000000
		# create a shared numpy array
		data_proxy = manager.ArrayHelper ((10, 10))
		print ( f'Array created on host: {data_proxy}' )
		# confirm content
		print ( f'Array sum: {data_proxy.sum ()}' )
		# access data in the array
		# data_proxy.setdata ( slice ( 1, 3 ), 880 )
		data_proxy.setOnedata(1,3, 403)
		print ( data_proxy.getdata ( slice ( 0, 10 ) ) )


		process = Process ( target=task, args=(data_proxy,) )

		process.start ()

		process.join ()

		# print ( 'Out', data_proxy.getdata(slice(0,10)))