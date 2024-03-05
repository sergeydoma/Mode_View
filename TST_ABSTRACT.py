import sys
import time
from multiprocessing import Process
from multiprocessing.managers import BaseManager

import numpy as np
from PySide6.QtCore import QAbstractTableModel, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView


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

    def setData(self, _data):
        self.model = PandasModel(_data)
        self.table.setModel(self.model)
        self.setCentralWidget(self.table)
        self.model.layoutChanged.emit()




data = np.array([
  [1, 9, 2],
  [1, 0, -1],
  [3, 5, 2],
  [3, 3, 2],
  [5, 8, 9],
])
i = 0

class CustomManager (BaseManager):
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
    def getArray(self):
        return self.array

    # call functions on the numpy array
    def sum(self):
        return self.array.sum ()

def task(data_proxy):
    for i in range(3):
    # while (True):
        global data
        # report details of the array
        print(f'Array sum (in child): {data_proxy.sum ()}')
        data_proxy.setOnedata(1, 3, 803+i)
        print('Tack', data_proxy.getdata(slice(0, 10 ) ) )
        data = data_proxy.getdata(slice(0, 10))
        time.sleep(1)
# for i in range (33):
#     i=i+1
#     print("OB1 =", i)
print (data)

def visu(data_proxy):
    # global data
    global i
    i = i+1
    print("циклы = ", i)
    # data = data_proxy.data_proxy.getdata ( slice ( 0, 10 ) ) )
    app = QApplication(sys.argv)
    window = MainWindow()
    print("visu", data_proxy.getdata(slice(0, 10)))

    # window.setData(data_proxy.getArray)
    # global data = data_proxy.getArray ()
    # print("visu", data_proxy.getdata(slice(0, 10 )))
    window.show ()
    data = data_proxy.getdata ( slice ( 0, 10 ) )
    window.setData (data)
    app.exec ()
    # if 1 == 1:
CustomManager.register ( 'ArrayHelper', ArrayHelper )
    # create and start the custom manager
# with
with CustomManager() as manager:
    data_proxy = manager.ArrayHelper((10, 10))
    print(f'Array created on host: {data_proxy}')
    # confirm content
    print(f'Array sum:{data_proxy.sum()}')
    # access data in the array
    # data_proxy.setdata ( slice ( 1, 3 ), 880 )
    data_proxy.setOnedata(1, 3, 403)
    # print ( data_proxy.getdata ( slice ( 0, 10 ) ) )
    # data = data_proxy.getArray()

    print("data_proxy =", data)

    process_2 = Process(target=visu, args=(data_proxy,), daemon= True)
    process_1 = Process(target=task, args=(data_proxy,), daemon= True)

    process_2.start()
    process_1.start()
    # process_1.join ()
    process_2.join()

print ('DATA=',data)
# process_2 = Process ( target=visu, args=(data_proxy) )
# process_2.start()
# process_2.join ()