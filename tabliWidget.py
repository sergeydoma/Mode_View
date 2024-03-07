# share 2d numpy array via a shared array
import sys
import time

from multiprocessing import Process
from multiprocessing.sharedctypes import RawArray

import numpy as np
from PySide6 import QtWidgets
from PySide6.QtCore import QAbstractTableModel, Qt, QTimer
from PySide6.QtWidgets import QTableView, QMainWindow, QApplication, QTableWidgetItem
from numpy import frombuffer
from numpy import double
from edit_dialog import Ui_MainWindow


class MainWindow (QtWidgets.QMainWindow,Ui_MainWindow):
	def __init__(self):
		super ().__init__ ()
		# Ui_MainWindow.__init__()
		self.setupUi( self )
		self.timer = QTimer ()
		self.timer.start (60 * 1000)
		self.timer.timeout.connect ( self.update_table )

	# self.update_table()
	# self.model.select()
	def update_table(self):
		# self.tblitems_1.setItem(1, 1, QTableWidgetItem(str (value)))



# task executed in a child process
def task(array):
	# create a new numpy array backed by the raw array
	data = frombuffer ( array, dtype=double, count=len ( array ) )
	# reshape array into preferred shape
	data = data.reshape ( (10, 10) )
	# check the contents
	print ( f'Child\n{data}' )
	# increment the data
	while (True):
		data[:] += 1
		# data[1][1] = 300
		# confirm change
		print ( f'Child\n{data}' )
		time.sleep ( 1 )


def visu(array):
	app = QApplication ( sys.argv )
	window = MainWindow ()
	# window.show ()

	data = frombuffer ( array, dtype=double, count=len ( array ) )
	# reshape array into preferred shape
	data = data.reshape ( (10, 10) )
	# while(True):
	data[1][1] = 400
	print ( f'Visu\n{data}' )
	# time.sleep(1)
	window.update_table()
	# print('data 00 = ', data[0][0])
	window.show ()


	# window.model.load_data(data)

	app.exec ()


# protect the entry point
if 1 == 1:
	# define the size of the numpy array
	n = 10 * 10
	# create the shared array
	array = RawArray ( 'd', n )
	# create a new numpy array backed by the raw array
	data = frombuffer ( array, dtype=double, count=len(array))
	# reshape array into preferred shape
	data = data.reshape((10, 10))
	# populate the array
	data.fill ( 1.0 )
	# confirm contents of the new array
	print ( f'Parent\n{data}' )
	# create a child process
	child1 = Process(target=task, args=(array,), daemon=True )
	child2 = Process(target=visu, args=(array,), daemon=True )
	# start the child process
	child1.start ()
	child2.start ()
	# wait for the child process to complete
	child2.join ()
	# check some data in the shared array

	print ( f'Parent\n{data}' )