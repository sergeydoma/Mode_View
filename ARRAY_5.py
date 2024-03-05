# share 2d numpy array via a shared array
import sys
import time
from multiprocessing import Process
from multiprocessing.sharedctypes import RawArray

import numpy as np
from PySide6 import QtCore
from PySide6.QtCore import QAbstractTableModel, Qt, QTimer
from PySide6.QtWidgets import QTableView, QMainWindow, QApplication
from numpy import frombuffer
from numpy import double

#region Absract Model
class PandasModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    # def update_data(self, data):
    #         #changes data in column 1 and 3
    #         #data updates 10x per second
    #         self.beginResetModel()
    #         self.data = data
    #         self.endResetModel()

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




    # def load_data(self, data):
    #     self.beginResetModel()
    #     self.input_address = data[0]
    #     self.input_numbers = data[1]
    #     self.column_count = 2
    #     self.row_count = len(self.input_numbers)
    #     self.endResetModel()

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable
#endregion

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.table = QTableView()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_table)

        # self.timer.timeout(self.update_table)
        self.timer.start(60 * 10)

        # self.update_table()
        # self.model.select()
    def update_table(self):
        # self.beginResetModel()
        self.model = PandasModel(data)
        self.model.dataChanged.emit( QtCore.QModelIndex(), QtCore.QModelIndex())
        # self.model.setData(self, 1, 1)
        # self.model.load_data(data)


        # self.update_table()
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)
        self.model.dataChanged.emit ( QtCore.QModelIndex (), QtCore.QModelIndex () )
        # self.table.close()
        # self.table.show()
        # self.endResetModel()
        # self.tableView.setModel(PandasModel)
        # time.sleep(5)

data = np.array([
  [1, 9, 2],
  [1, 0, -1],
  [3, 5, 2],
  [3, 3, 2],
  [5, 8, 9],
])

# task executed in a child process
def task(array):
    # create a new numpy array backed by the raw array
    data = frombuffer(array, dtype=double, count=len(array))
    # reshape array into preferred shape
    data = data.reshape((26, 10))
    # check the contents
    print(f'Child\n{data}')
    # increment the data
    while (True):
        data[:] += 1
        data[1][1] = 300
        # confirm change
        print(f'Child\n{data}')
        time.sleep(1)

def visu(array):

    data = frombuffer(array, dtype=double, count=len(array))
    # reshape array into preferred shape
    data = data.reshape((26, 10))
    # while(True):
    data[1][1] = 400+1
    # print(f'Visu\n{data}')
    # time.sleep(1)
    app = QApplication (sys.argv)
    window = MainWindow ()
    window.show()
    window.update_table()
    # time.sleep(1)
    app.exec()

# protect the entry point
if 1 == 1:
    # define the size of the numpy array
    n = 26 * 10
    # create the shared array
    array = RawArray('d', n)
    # create a new numpy array backed by the raw array

    data = frombuffer(array, dtype=double, count=len(array))
    # reshape array into preferred shape
    data = data.reshape((26, 10))
    # populate the array
    data.fill(1.0)
    # confirm contents of the new array
    print(f'Parent\n{data}')
    # create a child process
    child1 = Process(target=task, args=(array,), daemon= False)
    child2 = Process(target=visu, args=(array,), daemon=True)
    # start the child process
    child2.start()
    child1.start()
    # wait for the child process to complete
    child2.join()
    # check some data in the shared array

    print(f'Parent\n{data}')