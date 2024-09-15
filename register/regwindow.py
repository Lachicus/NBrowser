# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'regwPDXKm.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import res.loginReg.logosrc_rc

class Ui_RegWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
            MainWindow.setWindowFlags(Qt.FramelessWindowHint)
            MainWindow.setAttribute(Qt.WA_TranslucentBackground)
        MainWindow.resize(311, 435)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 290, 411))
        font = QFont()
        font.setBold(False)
        font.setItalic(False)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"background-color:rgba(6, 1, 28, 225);\n"
"border-radius:8px;")
        self.txt_passcode = QLineEdit(self.centralwidget)
        self.txt_passcode.setObjectName(u"txt_passcode")
        self.txt_passcode.setGeometry(QRect(30, 240, 250, 30))
        font1 = QFont()
        font1.setPointSize(10)
        self.txt_passcode.setFont(font1)
        self.txt_passcode.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,225);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 180, 271, 20))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(90, 40, 131, 121))
        self.logo.setStyleSheet(u"image: url(:/logo/logo.png);")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 340, 111, 31))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.pushButton.setFont(font2)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(9, 57, 104);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(12, 91, 171);\n"
"}\n"
"\n"
"\n"
"")
        self.txt_passcode_2 = QLineEdit(self.centralwidget)
        self.txt_passcode_2.setObjectName(u"txt_passcode_2")
        self.txt_passcode_2.setGeometry(QRect(30, 290, 250, 30))
        self.txt_passcode_2.setFont(font1)
        self.txt_passcode_2.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,225);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px")
        self.btn_exit = QPushButton(self.centralwidget)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setGeometry(QRect(170, 340, 111, 31))
        font3 = QFont()
        font3.setBold(True)
        self.btn_exit.setFont(font3)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setAutoFillBackground(False)
        self.btn_exit.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(163, 11, 42);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(240, 12, 58);\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText("")
        self.txt_passcode.setText("")
        self.txt_passcode.setPlaceholderText(QCoreApplication.translate("MainWindow", u"4 Digit Passcode", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Enter your prefered passcode", None))
        self.logo.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.txt_passcode_2.setText("")
        self.txt_passcode_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm Passcode", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.txt_passcode.setEchoMode(QLineEdit.Password)
        self.txt_passcode_2.setEchoMode(QLineEdit.Password)
        self.txt_passcode.setValidator(QIntValidator(1, 1000))
        self.txt_passcode_2.setValidator(QIntValidator(1, 1000))
    # retranslateUi

