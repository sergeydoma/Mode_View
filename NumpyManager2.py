# access data via array index in hosted numpy array
from multiprocessing.managers import BaseManager
from numpy import ones


# custom manager to support custom classes
class CustomManager ( BaseManager ):
	# nothing
	pass


# helper wrapping a numpy array
class ArrayHelper ():
	def __init__(self, dim):
		self.array = ones(dim)

	# access array data by slice
	def getdata(self, array_slice):
		return self.array[array_slice]

	def setdata(self, array_slice, value):
		self.array[array_slice] = value

	# call functions on the numpy array
	def sum(self):
		return self.array.sum ()


# protect the entry point
if 1 == 1:
	# register the a python class with the custom manager
	CustomManager.register ( 'ArrayHelper', ArrayHelper )
	# create and start the custom manager
	with CustomManager () as manager:
		# define the size of the numpy array
		n = 100000000
		# create a shared numpy array
		data_proxy = manager.ArrayHelper ( (n,) )
		print ( f'Array created on host: {data_proxy}' )
		# confirm content
		print ( f'Array sum: {data_proxy.sum ()}' )
		# access data in the array
		data_proxy.setdata(slice(2,3),880)
		print ( data_proxy.getdata ( slice ( 0, 10 ) ) )