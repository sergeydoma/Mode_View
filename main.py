# share a numpy array between processes using a manager
from multiprocessing import Process
from multiprocessing.managers import BaseManager

import pandas as pd
from PySide6 import QtCore
from PySide6.QtCore import Qt
from numpy import ones
import numpy as np


#region _ Abstact Model

class TableModel ( QtCore.QAbstractTableModel ):
	def __init__(self, data):
		super ( TableModel, self ).__init__ ()
		self._data = data

	def data(self, index, role):
		if role == Qt.DisplayRole:
			value = self._data.iloc[index.row (), index.column ()]
			return str ( value )

	def rowCount(self, index):
		return self._data.shape[0]

	def columnCount(self, index):
		return self._data.shape[1]

	def headerData(self, section, orientation, role):
		# section is the index of the column/row.
		if role == Qt.DisplayRole:
			if orientation == Qt.Horizontal:
				return str ( self._data.columns[section] )
			if orientation == Qt.Vertical:
				return str ( self._data.index[section] )


# endregion
#region DataFrame
data = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	]
pd.DataFrame (data, columns=['Калал 1', 'Калал 2', 'Калал 3', 'Калал 4', 'Калал 5',
            'Калал 6', 'Калал 7', 'Калал 8', 'Калал 9', 'Калал 10'],
    index=['Режим работы:', 'Режим работы канала', 'Допустимые диапазоны:', 'Диапазон сопр. изоляции авар.',
           'Диапазон сопр. шлейфа авар.', 'Диапазон сопр. изоляции предупр.', 'Диапазон сопр. шлейфа предупр.',
           'Уставки:', 'Уставка напряжения на входе', 'Уставка сопр. изоляции 1', 'Уставка сопр. изоляции 2',
           'Уставка сопр. шлейфа', 'Текущие значения:', 'Сопр. изоляции 1', 'Сопр. изоляции 1',
           'Сопр. шлейфа', 'Напряжение на входе 1', 'Напряжение на входе 2',
           'Расчетное знач. объем. наряжение', 'Авария - "А", предупрежд. - "П"', 'Сопр. изоляции 1 ниже доп.',
           'Сопр. изоляции 2 ниже доп.', 'Сопр. шлейфа ниже доп.', 'Сопр. шлейфа выше доп.',
           'Напряжение на входе 1 выше доп.', 'Напряжение на входе 2 выше доп.'])
#endregion
# custom manager to support custom classes
class CustomManager ( BaseManager ):
	# nothing
	pass

	def ArrayHelper(self, param):
		pass


class ArrayHelper ():
	def __init__(self, dim):
		self.array = np.ones ( dim )

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
	for i in range ( 1 ):
		# report details of the array
		print ( f'Array sum (in child): {data_proxy.sum ()}' )
		data_proxy.setOnedata ( 1, 3, 803 )
		print ( 'Tack', data_proxy.getdata ( slice ( 0, 10 ) ) )


# protect the entry point
if __name__ == '__main__':
	# register the a python class with the custom manager
	CustomManager.register ( 'ArrayHelper', ArrayHelper )
	# create and start the custom manager
	with CustomManager () as manager:
		# define the size of the numpy array
		# n = 100000000
		# create a shared numpy array
		data_proxy = manager.ArrayHelper ( (10, 10) )
		print ( f'Array created on host: {data_proxy}' )
		# confirm content
		print ( f'Array sum: {data_proxy.sum ()}' )
		# access data in the array
		# data_proxy.setdata ( slice ( 1, 3 ), 880 )
		data_proxy.setOnedata ( 1, 3, 403 )
		print ( data_proxy.getdata ( slice ( 0, 10 ) ) )

		process = Process ( target=task, args=(data_proxy,) )

		process.start ()

		process.join ()

# print ( 'Out', data_proxy.getdata(slice(0,10)))
