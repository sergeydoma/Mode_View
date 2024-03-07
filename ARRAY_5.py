# share 2d numpy array via a shared array
import sys
import time
from multiprocessing import Process
from multiprocessing.sharedctypes import RawArray

import numpy as np
import pandas as pd
from PySide6 import QtCore, QtGui
from PySide6.QtCore import QAbstractTableModel, Qt, QTimer
from PySide6.QtWidgets import QTableView, QMainWindow, QApplication
from numpy import frombuffer
from numpy import double
from edit_dialog import Ui_MainWindow


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
                value = self._data.iloc[index.row(), index.column()]
                return str(value)
            if role == Qt.BackgroundRole and index.row() == 0:
                # See below for the data structure.
                return QtGui.QColor ('blue')
        if role == Qt.TextAlignmentRole:
            value = self._data.iloc[index.row()][index.column()]

            if isinstance ( value, int ) or isinstance ( value, float )or isinstance ( value, double ):
                # Align right, vertical middle.
                return Qt.AlignVCenter + Qt.AlignRight


    def setData(self, index, value, role):
        if role == Qt.EditRole:
            try:
                value = int(value)
            except ValueError:
                return False
            self._data.iloc[index.row(), index.column()] = value
            return True
        return False

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str (self._data.columns[section] )

            if orientation == Qt.Vertical:
                return str (self._data.index[section] )
#endregion

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.table = QTableView()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_table)
        # self.tableView_Arhive.setModel ( self.model )
        # self.timer.timeout(self.update_table)
        self.timer.start(60 * 10)

        # self.update_table()
        # self.model.select()
    def update_table(self):
        # self.beginResetModel()
        self.model1 = PandasModel(dataP1)
        self.model2 = PandasModel(dataP2)
        self.model1.dataChanged.emit( QtCore.QModelIndex(), QtCore.QModelIndex())
        # self.model.setData(self, 1, 1)
        # self.model.load_data(data)


        # self.update_table()
        # self.table.setModel(self.model)
        self.tableView_plat_1.setModel ( self.model1 )
        self.tableView_plat_2.setModel ( self.model2 )
        # self.setCentralWidget(self.table)
        self.model1.dataChanged.emit ( QtCore.QModelIndex (), QtCore.QModelIndex () )
        self.model2.dataChanged.emit ( QtCore.QModelIndex (), QtCore.QModelIndex () )
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
    dataAll = frombuffer(array, dtype=double, count=len(array))
    # reshape array into preferred shape
    dataAll = dataAll.reshape((26, 40))
    dataSumm = np.hsplit(dataAll, 4)
    dataP1 = dataSumm[0]
    dataP2 = dataSumm[1]
    dataP3 = dataSumm[2]
    dataP4 = dataSumm[3]
    # check the contents
    print(f'Child\n{dataP2}')
    # increment the data
    while (True):
        dataP1[:] += 1
        dataP1[1][1] =str(300)
        dataP2[:] += 20
        # confirm change
        print(f'Child\n{data}')
        time.sleep(1)

def visu(array):

    dataAll = frombuffer(array, dtype=double, count=len(array))
    # reshape array into preferred shape
    dataAll = dataAll.reshape((26, 40))
    dataSumm = np.hsplit(dataAll,4)
    # while(True):
    dataP1 = dataSumm[0]
    dataP2 = dataSumm[1]
    dataP3 = dataSumm[2]
    dataP4 = dataSumm[3]
    
    dataP1[1][2] = 25
    dataP2[1][2] = 500 + 1
    app = QApplication (sys.argv)
    window = MainWindow ()
    window.show()
    window.update_table()
    # time.sleep(1)
    app.exec()

# protect the entry point
if 1 == 1:
    # define the size of the numpy array
    n = 26 * 40
    # create the shared array
    array = RawArray('d', n)
    # create a new numpy array backed by the raw array

    dataAll = frombuffer(array, dtype=double, count=len(array))

    # reshape array into preferred shape
    dataAll = dataAll.reshape(26, 40)
    # populate the array
    dataAll.fill(1.0)
    dataSumm=np.hsplit(dataAll, 4)
    dataP1 = dataSumm[0]
    dataP2 = dataSumm[1]
    dataP3 = dataSumm[2]
    dataP4 = dataSumm[3]
    dataP1 = pd.DataFrame( dataP1,
      columns=['Калал 1', 'Калал 2', 'Калал 3', 'Калал 4', 'Калал 5',
                      'Калал 6', 'Калал 7', 'Калал 8', 'Калал 9', 'Калал 10'],
      index=['Режим работы:', 'Режим работы канала', 'Допустимые диапазоны:',
             'Диапазон сопр. изоляции авар.',
             'Диапазон сопр. шлейфа авар.', 'Диапазон сопр. изоляции предупр.',
             'Диапазон сопр. шлейфа предупр.',
             'Уставки:', 'Уставка напряжения на входе', 'Уставка сопр. изоляции 1',
             'Уставка сопр. изоляции 2',
             'Уставка сопр. шлейфа', 'Текущие значения:', 'Сопр. изоляции 1', 'Сопр. изоляции 1',
             'Сопр. шлейфа', 'Напряжение на входе 1', 'Напряжение на входе 2',
             'Расчетное знач. объем. наряжение', 'Авария - "А", предупрежд. - "П"',
             'Сопр. изоляции 1 ниже доп.',
             'Сопр. изоляции 2 ниже доп.', 'Сопр. шлейфа ниже доп.', 'Сопр. шлейфа выше доп.',
             'Напряжение на входе 1 выше доп.', 'Напряжение на входе 2 выше доп.'] )

    dataP2 = pd.DataFrame(dataP2,
                            columns=['Калал 1', 'Калал 2', 'Калал 3', 'Калал 4', 'Калал 5',
                                     'Калал 6', 'Калал 7', 'Калал 8', 'Калал 9', 'Калал 10'],
                            index=['Режим работы:', 'Режим работы канала', 'Допустимые диапазоны:',
                                   'Диапазон сопр. изоляции авар.',
                                   'Диапазон сопр. шлейфа авар.', 'Диапазон сопр. изоляции предупр.',
                                   'Диапазон сопр. шлейфа предупр.',
                                   'Уставки:', 'Уставка напряжения на входе', 'Уставка сопр. изоляции 1',
                                   'Уставка сопр. изоляции 2',
                                   'Уставка сопр. шлейфа', 'Текущие значения:', 'Сопр. изоляции 1', 'Сопр. изоляции 1',
                                   'Сопр. шлейфа', 'Напряжение на входе 1', 'Напряжение на входе 2',
                                   'Расчетное знач. объем. наряжение', 'Авария - "А", предупрежд. - "П"',
                                   'Сопр. изоляции 1 ниже доп.',
                                   'Сопр. изоляции 2 ниже доп.', 'Сопр. шлейфа ниже доп.', 'Сопр. шлейфа выше доп.',
                                   'Напряжение на входе 1 выше доп.', 'Напряжение на входе 2 выше доп.'] )


    # confirm contents of the new array
    print(f'Parent\n{data}')
    # create a child process
    child1 = Process(target=task, args=(array,), daemon=True)
    child2 = Process(target=visu, args=(array,), daemon=True)
    # start the child process
    child2.start()
    child1.start()
    # wait for the child process to complete
    child2.join()
    # check some data in the shared array

    print(f'Parent\n{data}')