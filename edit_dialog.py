# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(234, 285)
        self.cmbIndicator = QComboBox(Dialog)
        self.cmbIndicator.setObjectName(u"cmbIndicator")
        self.cmbIndicator.setGeometry(QRect(10, 40, 211, 22))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 71, 16))
        self.txtYear = QLineEdit(Dialog)
        self.txtYear.setObjectName(u"txtYear")
        self.txtYear.setGeometry(QRect(10, 100, 113, 21))
        self.txtValue = QLineEdit(Dialog)
        self.txtValue.setObjectName(u"txtValue")
        self.txtValue.setGeometry(QRect(10, 170, 113, 21))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 80, 49, 16))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 150, 71, 16))
        self.btnAdd = QPushButton(Dialog)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setGeometry(QRect(10, 230, 75, 24))
        self.btnCancel = QPushButton(Dialog)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setGeometry(QRect(110, 230, 75, 24))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Indicator", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Year", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Value", None))
        self.btnAdd.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.btnCancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

