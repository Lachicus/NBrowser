# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerKagavm.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import res.dashboard.icon2_rc

class Ui_Instance(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
            MainWindow.setWindowFlags(Qt.FramelessWindowHint)
            MainWindow.setAttribute(Qt.WA_TranslucentBackground)
        MainWindow.resize(1289, 735)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.anchor = QLabel(self.centralwidget)
        self.anchor.setObjectName(u"anchor")
        self.anchor.setGeometry(QRect(20, 10, 1251, 711))
        font = QFont()
        font.setBold(False)
        font.setItalic(False)
        self.anchor.setFont(font)
        self.anchor.setStyleSheet(u"background-color:rgba(6, 1, 28, 225);\n"
"border-radius:8px;")
        self.logo_2 = QLabel(self.centralwidget)
        self.logo_2.setObjectName(u"logo_2")
        self.logo_2.setGeometry(QRect(30, 30, 91, 81))
        self.logo_2.setStyleSheet(u"image: url(:/logos/logo.png);")
        self.btn_exit = QPushButton(self.centralwidget)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setGeometry(QRect(1240, 20, 21, 21))
        font1 = QFont()
        font1.setBold(True)
        self.btn_exit.setFont(font1)
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
        self.btn_minimize = QPushButton(self.centralwidget)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setGeometry(QRect(1210, 20, 21, 21))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.btn_minimize.setFont(font2)
        self.btn_minimize.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_minimize.setStyleSheet(u"QPushButton {\n"
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
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(40, 120, 71, 581))
        self.groupBox.setMinimumSize(QSize(71, 581))
        self.groupBox.setStyleSheet(u"color:rgb(250,250,250)")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(129, 49, 1121, 651))
        self.webcasing = QGridLayout(self.gridLayoutWidget)
        self.webcasing.setObjectName(u"webcasing")
        self.webcasing.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.anchor.setText("")
        self.logo_2.setText("")
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.btn_minimize.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Controls", None))
    # retranslateUi

