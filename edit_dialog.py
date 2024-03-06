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
        self.tabWidget.setGeometry(QRect(0, 20, 1421, 871))
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
        self.tblitems_2 = QTableWidget(self.tab_3)
        if (self.tblitems_2.columnCount() < 10):
            self.tblitems_2.setColumnCount(10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tblitems_2.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tblitems_2.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tblitems_2.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tblitems_2.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tblitems_2.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tblitems_2.setHorizontalHeaderItem(5, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tblitems_2.setHorizontalHeaderItem(6, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tblitems_2.setHorizontalHeaderItem(7, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tblitems_2.setHorizontalHeaderItem(8, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tblitems_2.setHorizontalHeaderItem(9, __qtablewidgetitem20)
        if (self.tblitems_2.rowCount() < 26):
            self.tblitems_2.setRowCount(26)
        font2 = QFont()
        font2.setBold(True)
        font2.setItalic(True)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font2);
        self.tblitems_2.setVerticalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font2);
        self.tblitems_2.setVerticalHeaderItem(2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(4, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(5, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(6, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setFont(font2);
        self.tblitems_2.setVerticalHeaderItem(7, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(8, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(9, __qtablewidgetitem30)
        icon = QIcon(QIcon.fromTheme(u"accessories-calculator"))
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setText(u"\u0423\u0441\u0442\u0430\u0432\u043a\u0430 \u0441\u043e\u043f\u0440. \u0438\u0437\u043e\u043b\u044f\u0446\u0438\u0438 2");
        __qtablewidgetitem31.setIcon(icon);
        self.tblitems_2.setVerticalHeaderItem(10, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(11, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setFont(font2);
        self.tblitems_2.setVerticalHeaderItem(12, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(13, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(14, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(15, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(16, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(17, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(18, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setFont(font2);
        self.tblitems_2.setVerticalHeaderItem(19, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(20, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(21, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(22, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(23, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(24, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(25, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        __qtablewidgetitem47.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled|Qt.ItemIsAutoTristate);
        self.tblitems_2.setItem(9, 0, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(20, 0, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(20, 1, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        __qtablewidgetitem50.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(20, 2, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(20, 3, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(20, 4, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(20, 5, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(20, 6, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        __qtablewidgetitem55.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(20, 7, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        __qtablewidgetitem56.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(20, 8, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        __qtablewidgetitem57.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(20, 9, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        __qtablewidgetitem58.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(21, 0, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        __qtablewidgetitem59.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(21, 1, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        __qtablewidgetitem60.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(21, 2, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        __qtablewidgetitem61.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(21, 3, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        __qtablewidgetitem62.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(21, 4, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        __qtablewidgetitem63.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(21, 5, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        __qtablewidgetitem64.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(21, 6, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        __qtablewidgetitem65.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(21, 7, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        __qtablewidgetitem66.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(21, 8, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        __qtablewidgetitem67.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(21, 9, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        __qtablewidgetitem68.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(22, 0, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        __qtablewidgetitem69.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(22, 1, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        __qtablewidgetitem70.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(22, 2, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        __qtablewidgetitem71.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(22, 3, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        __qtablewidgetitem72.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(22, 4, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        __qtablewidgetitem73.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(22, 5, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        __qtablewidgetitem74.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(22, 6, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        __qtablewidgetitem75.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(22, 7, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        __qtablewidgetitem76.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(22, 8, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        __qtablewidgetitem77.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(22, 9, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        __qtablewidgetitem78.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(23, 0, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        __qtablewidgetitem79.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(23, 1, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        __qtablewidgetitem80.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(23, 2, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        __qtablewidgetitem81.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(23, 3, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        __qtablewidgetitem82.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(23, 4, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        __qtablewidgetitem83.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(23, 5, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        __qtablewidgetitem84.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(23, 6, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        __qtablewidgetitem85.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(23, 7, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        __qtablewidgetitem86.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(23, 8, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        __qtablewidgetitem87.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(23, 9, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        __qtablewidgetitem88.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(24, 0, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        __qtablewidgetitem89.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(24, 1, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        __qtablewidgetitem90.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(24, 2, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        __qtablewidgetitem91.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(24, 3, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        __qtablewidgetitem92.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(24, 4, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        __qtablewidgetitem93.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(24, 5, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        __qtablewidgetitem94.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(24, 6, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        __qtablewidgetitem95.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(24, 7, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        __qtablewidgetitem96.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(24, 8, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        __qtablewidgetitem97.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(24, 9, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        __qtablewidgetitem98.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(25, 0, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        __qtablewidgetitem99.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(25, 1, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        __qtablewidgetitem100.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(25, 2, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        __qtablewidgetitem101.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(25, 3, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        __qtablewidgetitem102.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(25, 4, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        __qtablewidgetitem103.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(25, 5, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        __qtablewidgetitem104.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(25, 6, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        __qtablewidgetitem105.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(25, 7, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        __qtablewidgetitem106.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(25, 8, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        __qtablewidgetitem107.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(25, 9, __qtablewidgetitem107)
        self.tblitems_2.setObjectName(u"tblitems_2")
        self.tblitems_2.setGeometry(QRect(0, 0, 1411, 881))
        self.tblitems_2.setFont(font)
        self.tblitems_2.setLayoutDirection(Qt.LeftToRight)
        self.tblitems_2.setShowGrid(True)
        self.tblitems_2.setGridStyle(Qt.SolidLine)
        self.tblitems_2.setSortingEnabled(False)
        self.tblitems_2.setRowCount(26)
        self.tblitems_2.horizontalHeader().setVisible(True)
        self.tblitems_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tblitems_2.horizontalHeader().setMinimumSectionSize(90)
        self.tblitems_2.horizontalHeader().setDefaultSectionSize(110)
        self.tblitems_2.horizontalHeader().setHighlightSections(True)
        self.tblitems_2.horizontalHeader().setProperty("showSortIndicator", True)
        self.tblitems_2.horizontalHeader().setStretchLastSection(False)
        self.tblitems_2.verticalHeader().setVisible(True)
        self.tblitems_2.verticalHeader().setCascadingSectionResizes(False)
        self.tblitems_2.verticalHeader().setHighlightSections(True)
        self.tblitems_2.verticalHeader().setProperty("showSortIndicator", False)
        self.tblitems_2.verticalHeader().setStretchLastSection(False)
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
        ___qtablewidgetitem11 = self.tblitems_2.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 1", None));
        ___qtablewidgetitem12 = self.tblitems_2.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 2", None));
        ___qtablewidgetitem13 = self.tblitems_2.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 3", None));
        ___qtablewidgetitem14 = self.tblitems_2.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 4", None));
        ___qtablewidgetitem15 = self.tblitems_2.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 5", None));
        ___qtablewidgetitem16 = self.tblitems_2.horizontalHeaderItem(5)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 6", None));
        ___qtablewidgetitem17 = self.tblitems_2.horizontalHeaderItem(6)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 7", None));
        ___qtablewidgetitem18 = self.tblitems_2.horizontalHeaderItem(7)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 8", None));
        ___qtablewidgetitem19 = self.tblitems_2.horizontalHeaderItem(8)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 9", None));
        ___qtablewidgetitem20 = self.tblitems_2.horizontalHeaderItem(9)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 10", None));
        ___qtablewidgetitem21 = self.tblitems_2.verticalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0436\u0438\u043c\u044b \u0440\u0430\u0431\u043e\u0442\u044b:", None));
        ___qtablewidgetitem22 = self.tblitems_2.verticalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0436\u0438\u043c \u0440\u0430\u0431\u043e\u0442\u044b \u043a\u0430\u043d\u0430\u043b\u0430", None));
        ___qtablewidgetitem23 = self.tblitems_2.verticalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043f\u0443\u0441\u0442\u0438\u043c\u044b\u0435 \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d\u044b:", None));
        ___qtablewidgetitem24 = self.tblitems_2.verticalHeaderItem(3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u0441\u043e\u043f\u0440. \u0438\u0437\u043e\u043b\u044f\u0446\u0438\u0438 \u0430\u0432\u0430\u0440.", None));
        ___qtablewidgetitem25 = self.tblitems_2.verticalHeaderItem(4)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u0441\u043e\u043f\u0440. \u0448\u043b\u0435\u0439\u0444\u0430 \u0430\u0432\u0430\u0440.", None));
        ___qtablewidgetitem26 = self.tblitems_2.verticalHeaderItem(5)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u0441\u043e\u043f\u0440. \u0438\u0437\u043e\u043b\u044f\u0446\u0438\u0438 \u043f\u0440\u0435\u0434\u0443\u043f\u0440.", None));
        ___qtablewidgetitem27 = self.tblitems_2.verticalHeaderItem(6)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u0441\u043e\u043f\u0440. \u0448\u043b\u0435\u0439\u0444\u0430 \u043f\u0440\u0435\u0434\u0443\u043f\u0440.", None));
        ___qtablewidgetitem28 = self.tblitems_2.verticalHeaderItem(7)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u0432\u043a\u0438:", None));
        ___qtablewidgetitem29 = self.tblitems_2.verticalHeaderItem(8)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u0432\u043a\u0430 \u043d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u044f \u043d\u0430 \u0432\u0445\u043e\u0434\u0435", None));
        ___qtablewidgetitem30 = self.tblitems_2.verticalHeaderItem(9)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u0432\u043a\u0430 \u0441\u043e\u043f\u0440. \u0438\u0437\u043e\u043b\u044f\u0446\u0438\u0438 1", None));
        ___qtablewidgetitem31 = self.tblitems_2.verticalHeaderItem(11)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u0432\u043a\u0430 \u0441\u043e\u043f\u0440. \u0448\u043b\u0435\u0439\u0444\u0430", None));
        ___qtablewidgetitem32 = self.tblitems_2.verticalHeaderItem(12)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f:", None));
        ___qtablewidgetitem33 = self.tblitems_2.verticalHeaderItem(13)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043f\u0440. \u0438\u0437\u043e\u043b\u044f\u0446\u0438\u0438 1", None));
        ___qtablewidgetitem34 = self.tblitems_2.verticalHeaderItem(14)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043f\u0440. \u0438\u0437\u043e\u043b\u044f\u0446\u0438\u0438 2", None));
        ___qtablewidgetitem35 = self.tblitems_2.verticalHeaderItem(15)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043f\u0440. \u0448\u043b\u0435\u0439\u0444\u0430", None));
        ___qtablewidgetitem36 = self.tblitems_2.verticalHeaderItem(16)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u0435 \u043d\u0430 \u0432\u0445\u043e\u0434\u0435 1", None));
        ___qtablewidgetitem37 = self.tblitems_2.verticalHeaderItem(17)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u0435 \u043d\u0430 \u0432\u0445\u043e\u0434\u0435 2", None));
        ___qtablewidgetitem38 = self.tblitems_2.verticalHeaderItem(18)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0435\u0442\u043d\u043e\u0435 \u0437\u043d\u0430\u0447. \u043e\u0431\u044a\u0435\u043c. \u043d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u044f", None));
        ___qtablewidgetitem39 = self.tblitems_2.verticalHeaderItem(19)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0430\u0440\u0438\u044f - \"\u0410\", \u043f\u0440\u0435\u0434\u0443\u043f\u0440\u0436\u0434. - \"\u041f\":", None));
        ___qtablewidgetitem40 = self.tblitems_2.verticalHeaderItem(20)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043f\u0440\u043e\u0442\u0438\u0432\u043b\u0435\u043d\u0438\u0435 \u0438\u0437\u043e\u043b\u044f\u0446\u0438\u0438 1 < \u0434\u043e\u043f.", None));
        ___qtablewidgetitem41 = self.tblitems_2.verticalHeaderItem(21)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043f\u0440\u043e\u0442\u0438\u0432\u043b\u0435\u043d\u0438\u0435 \u0438\u0437\u043e\u043b\u044f\u0446\u0438\u0438 2 < \u0434\u043e\u043f.", None));
        ___qtablewidgetitem42 = self.tblitems_2.verticalHeaderItem(22)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043f\u0440\u043e\u0442\u0438\u0432\u043b\u0435\u043d\u0438\u0435 \u0448\u043b\u0435\u0439\u0444\u0430 < \u0434\u043e\u043f.", None));
        ___qtablewidgetitem43 = self.tblitems_2.verticalHeaderItem(23)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043f\u0440\u043e\u0442\u0438\u0432\u043b\u0435\u043d\u0438\u0435 \u0448\u043b\u0435\u0439\u0444\u0430 > \u0434\u043e\u043f.", None));
        ___qtablewidgetitem44 = self.tblitems_2.verticalHeaderItem(24)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u0435 1 \u0432\u044b\u0448\u0435 \u0434\u043e\u043f\u0443\u0441\u043a", None));
        ___qtablewidgetitem45 = self.tblitems_2.verticalHeaderItem(25)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u0435 2 \u0432\u044b\u0448\u0435 \u0434\u043e\u043f\u0443\u0441\u043a", None));

        __sortingEnabled = self.tblitems_2.isSortingEnabled()
        self.tblitems_2.setSortingEnabled(False)
        self.tblitems_2.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u041f\u043b\u0430\u0442\u0430 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u0410\u0440\u0445\u0438\u0432", None))
    # retranslateUi

