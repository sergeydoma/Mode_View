# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pmk20_001.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QTableView,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1416, 954)
        MainWindow.setStyleSheet(u"background-color: rgb(213, 213, 159);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 10, 1421, 871))
        font = QFont()
        font.setFamilies([u"Sans Serif"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(Qt.ClickFocus)
        self.tabWidget.setStyleSheet(u"font: 12pt \"Sans Serif\";\n"
"background-color: rgb(234, 232, 220);\n"
"color: rgb(0, 0, 0);")
        self.tabWidget.setDocumentMode(False)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.tableWidget = QTableWidget(self.tab_1)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.tableWidget.rowCount() < 10):
            self.tableWidget.setRowCount(10)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignJustify|Qt.AlignVCenter);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem10)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(870, 10, 521, 331))
        font1 = QFont()
        font1.setFamilies([u"Sans Serif"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setKerning(True)
        font1.setHintingPreference(QFont.PreferFullHinting)
        self.tableWidget.setFont(font1)
        self.tableWidget.setStyleSheet(u"border-color: rgb(0, 85, 0);")
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(300)
        self.label_info = QLabel(self.tab_1)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setGeometry(QRect(80, 50, 431, 151))
        self.label_info.setStyleSheet(u"border-color: rgb(170, 170, 0);")
        self.label_info.setFrameShape(QFrame.Box)
        self.label_info.setFrameShadow(QFrame.Plain)
        self.label_info.setLineWidth(1)
        self.layoutWidget = QWidget(self.tab_1)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(70, 241, 293, 60))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.comboBox_1 = QComboBox(self.layoutWidget)
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.setObjectName(u"comboBox_1")

        self.gridLayout.addWidget(self.comboBox_1, 1, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.layoutWidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 1, 1)

        self.Button_con = QPushButton(self.layoutWidget)
        self.Button_con.setObjectName(u"Button_con")
        self.Button_con.setStyleSheet(u"background-color: rgb(213, 213, 159);")

        self.gridLayout.addWidget(self.Button_con, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tableView_plat_1 = QTableView(self.tab_2)
        self.tableView_plat_1.setObjectName(u"tableView_plat_1")
        self.tableView_plat_1.setGeometry(QRect(0, 0, 1401, 831))
        self.tableView_plat_1.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(234, 232, 220);\n"
"")
        self.tableView_plat_1.setLineWidth(3)
        self.tableView_plat_1.setMidLineWidth(2)
        self.tableView_plat_1.setSortingEnabled(True)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tableView_plat_2 = QTableView(self.tab_3)
        self.tableView_plat_2.setObjectName(u"tableView_plat_2")
        self.tableView_plat_2.setGeometry(QRect(0, 0, 1401, 831))
        self.tableView_plat_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(234, 232, 220);\n"
"")
        self.tableView_plat_2.setLineWidth(3)
        self.tableView_plat_2.setMidLineWidth(2)
        self.tableView_plat_2.setSortingEnabled(True)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tableView_Arhive = QTableView(self.tab_4)
        self.tableView_Arhive.setObjectName(u"tableView_Arhive")
        self.tableView_Arhive.setGeometry(QRect(10, 1, 1391, 841))
        self.tableView_Arhive.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(234, 232, 220);\n"
"")
        self.tableView_Arhive.setLineWidth(3)
        self.tableView_Arhive.setMidLineWidth(2)
        self.tableView_Arhive.setSortingEnabled(True)
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setToolTip("")
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None));
        ___qtablewidgetitem1 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0436\u0438\u043c \u0440\u0430\u0431\u043e\u0442\u044b \u043f\u0440\u0438\u0431\u043e\u0440\u0430", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0432\u0435\u0440\u0441\u0438\u0438 \u041f\u041e", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"ID \u0448\u0430\u0441\u0441\u0438", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"ID \u041f\u043b\u0430\u0442\u044b 1", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"ID \u041f\u043b\u0430\u0442\u044b 2", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0440\u043e\u043b\u044c\u043d\u0430\u044f \u0441\u0443\u043c\u043c\u0430 \u041f\u041e MD5", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0430\u0440\u0438\u044f", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0430\u0440\u0438\u044f +100 \u0412", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0430\u0440\u0438\u044f -100 \u0412", None));
        self.label_info.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0430 \u043d\u0430 \u0448\u0438\u043d\u0435 Modbus", None))
        self.comboBox_1.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.comboBox_1.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_1.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_1.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_1.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_1.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_1.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_1.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_1.setItemText(8, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_1.setItemText(9, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_1.setItemText(10, QCoreApplication.translate("MainWindow", u"a", None))
        self.comboBox_1.setItemText(11, QCoreApplication.translate("MainWindow", u"b", None))
        self.comboBox_1.setItemText(12, QCoreApplication.translate("MainWindow", u"c", None))
        self.comboBox_1.setItemText(13, QCoreApplication.translate("MainWindow", u"d", None))
        self.comboBox_1.setItemText(14, QCoreApplication.translate("MainWindow", u"e", None))
        self.comboBox_1.setItemText(15, QCoreApplication.translate("MainWindow", u"f", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"d", None))

        self.Button_con.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"\u041f\u041c\u041a-20", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u041f\u043b\u0430\u0442\u0430 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u041f\u043b\u0430\u0442\u0430 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u0410\u0440\u0445\u0438\u0432", None))
    # retranslateUi

