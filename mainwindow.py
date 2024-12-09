# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1033, 552)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btnAdd = QPushButton(self.centralwidget)
        self.btnAdd.setObjectName(u"btnAdd")

        self.gridLayout_2.addWidget(self.btnAdd, 0, 0, 1, 1)

        self.btnRemove = QPushButton(self.centralwidget)
        self.btnRemove.setObjectName(u"btnRemove")

        self.gridLayout_2.addWidget(self.btnRemove, 0, 1, 1, 1)

        self.btnEdit = QPushButton(self.centralwidget)
        self.btnEdit.setObjectName(u"btnEdit")

        self.gridLayout_2.addWidget(self.btnEdit, 0, 2, 1, 1)

        self.cmbYear = QComboBox(self.centralwidget)
        self.cmbYear.setObjectName(u"cmbYear")

        self.gridLayout_2.addWidget(self.cmbYear, 1, 2, 1, 1)

        self.lstitems = QListWidget(self.centralwidget)
        self.lstitems.setObjectName(u"lstitems")

        self.gridLayout_2.addWidget(self.lstitems, 2, 0, 1, 3)

        self.cmbIndicator = QComboBox(self.centralwidget)
        self.cmbIndicator.setObjectName(u"cmbIndicator")

        self.gridLayout_2.addWidget(self.cmbIndicator, 1, 0, 1, 2)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lblStatistics = QLabel(self.groupBox)
        self.lblStatistics.setObjectName(u"lblStatistics")

        self.gridLayout.addWidget(self.lblStatistics, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 3, 0, 1, 3)

        self.chartView = QChartView(self.centralwidget)
        self.chartView.setObjectName(u"chartView")

        self.gridLayout_2.addWidget(self.chartView, 0, 3, 4, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1033, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnAdd.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.btnRemove.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.btnEdit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Profitability", None))
        self.lblStatistics.setText("")
    # retranslateUi

