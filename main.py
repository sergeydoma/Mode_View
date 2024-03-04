# share a numpy array between processes using a manager
import sys

import numpy as np
from PySide6.QtCore import QAbstractTableModel, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView

from multiprocessing.managers import BaseManager
from edit_dialog import Ui_MainWindow

import pandas as pd
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt
from numpy import ones
import numpy as np

import sys
import time
from threading import Thread

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import QAbstractTableModel, Qt

from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QTableView
# from visuPmk import Visu_ui
import pandas as pd
from multiprocessing import Process
# from exchange import process_mb as p_mb


#region _ Abstact Model
class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole or role == Qt.EditRole:
                value = self._data[index.row(), index.column()]
                return str(value)

    def setData(self, index, value, role):
        if role == Qt.EditRole:
            try:
                value = int(value)
            except ValueError:
                return False
            self._data[index.row(), index.column()] = value
            return True
        return False

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

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
pd.DataFrame(data, columns=['Калал 1', 'Калал 2', 'Калал 3', 'Калал 4', 'Калал 5',
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
#region MAIN
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        # Visu_ui.__init__(self)
        self.setupUi(self)
        # self.writeTabl()
        # self.threadpool = QThreadPool ()
        # print ( "Multithreading with maximum %d threads" % self.threadpool.maxThreadCount ())
        self.tableView_Arhive

        self.model = TableModel(data)
        self.tableView_Arhive.setModel(self.model)
        self.setCentralWidget(self.tableView_Arhive)
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

def visu():
    app = QtWidgets.QApplication ( sys.argv )
    window = MainWindow ()
    window.show ()
    app.exec ()
    # data_proxy.setOnedata ( 1, 3, 703 )
    # print ( 'visu', data_proxy.getdata ( slice ( 0, 10 ) ) )

# protect the entry point
if __name__ == '__main__':
    # app = QtWidgets.QApplication(sys.argv)
    # window = MainWindow()
    # window.show()
    # app.exec()

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

        process1 = Process ( target=task, args=(data_proxy,) )

        process2 = Process ( target=visu, args=() )

        process1.start ()

        process2.start ()

        process1.join ()

# print ( 'Out', data_proxy.getdata(slice(0,10)))
