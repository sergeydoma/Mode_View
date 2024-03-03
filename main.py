import sys
import time
from asyncio import Queue
from multiprocessing import Process, set_start_method

import numpy as np
from PySide6 import QtWidgets
from PySide6.QtCore import QAbstractTableModel, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView
from numpy import ones


class PandasModel(QAbstractTableModel):
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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QTableView()


        # data = np.array([
        #   [1, 9, 2],
        #   [1, 0, -1],
        #   [3, 5, 2],
        #   [3, 3, 2],
        #   [5, 8, 9],
        # ])


        self.model = PandasModel(data)
        self.table.setModel(self.model)
        self.setCentralWidget(self.table)

    def saveData(self,row,column,value):
        data[row,column] = value

def task():
    # declare the global variable
    global data
    # check some data in the array
    # print ( data[:5, :5] )
    # change data in the array
    data.fill = np.array([
    [1, 9, 2],
    [1, 0, -1],
    [3, 5, 2],
    [3, 3, 2],
    [5, 8, 9],
    ])

# data = np.array ( [
#     [1, 9, 2],
#     [1, 0, -1],
#     [3, 5, 2],
#     [3, 3, 2],
#     [5, 8, 9],
# ] )
        # data[1,1] =99

# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# # data[1] = [55,33,22]
# app.exec()

# def appvisu():
#     app = QtWidgets.QApplication ( sys.argv )
#     window = MainWindow ()
#     window.show()
#     # data[1] = [55, 33, 22]
#     # window.saveData(2,2,567)
#     app.exec()


def exchang():
    # while (True):
    for i in range(1, 15):
        data[1,1] = i
        print("data = ", i)
        time.sleep(1)
        # data[1,1] = 55

if __name__ == '__main__':

    set_start_method('fork')

    data = ones ( (5, 3) )
    # data = = np.array ( [
    #     [1, 9, 2],
    #     [1, 0, -1],
    #     [3, 5, 2],
    #     [3, 3, 2],
    #     [5, 8, 9],
    # ] )

    th2 = Process(target=exchang, args=(), daemon=True)

    th2.start()

    app = QtWidgets.QApplication (sys.argv)
    window = MainWindow ()
    window.show()
    # data[1] = [55, 33, 22]
    # window.saveData(2,2,567)
    app.exec()

    q = Queue()



    # th2 = Process(target=exchang, args=(), daemon=True)
    # th2.start()

    # th1 = Process ( target=appvisu, args=(), daemon=True )
    # th1.start ()


    # th1.join()