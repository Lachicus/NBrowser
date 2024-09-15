# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NdashboardcrvtpJ.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import res.dashboard.logo_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
            MainWindow.setWindowFlags(Qt.FramelessWindowHint)
            MainWindow.setAttribute(Qt.WA_TranslucentBackground)
        MainWindow.resize(363, 738)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 20, 341, 711))
        font = QFont()
        font.setBold(False)
        font.setItalic(False)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"background-color:rgba(6, 1, 28, 225);\n"
"border-radius:8px;")
        self.btn_minimize = QPushButton(self.centralwidget)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setGeometry(QRect(290, 30, 21, 21))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.btn_minimize.setFont(font1)
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
        self.btn_exit = QPushButton(self.centralwidget)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setGeometry(QRect(320, 30, 21, 21))
        font2 = QFont()
        font2.setBold(True)
        self.btn_exit.setFont(font2)
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
        self.logo_2 = QLabel(self.centralwidget)
        self.logo_2.setObjectName(u"logo_2")
        self.logo_2.setGeometry(QRect(30, 40, 91, 81))
        self.logo_2.setStyleSheet(u"image: url(:/images/logo.png);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 70, 161, 20))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 140, 301, 161))
        self.groupBox.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_nhentai = QPushButton(self.groupBox)
        self.btn_nhentai.setObjectName(u"btn_nhentai")
        self.btn_nhentai.setGeometry(QRect(20, 30, 51, 51))
        self.btn_nhentai.setFont(font1)
        self.btn_nhentai.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_nhentai.setStyleSheet(u"QPushButton {\n"
"	image: url(:/images/nhentai.jpg);\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(9, 57, 104);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"image: url(:/images/logo.png);\n"
"	background-color: rgb(12, 91, 171);\n"
"}\n"
"\n"
"\n"
"")
        self.btn_hitomi = QPushButton(self.groupBox)
        self.btn_hitomi.setObjectName(u"btn_hitomi")
        self.btn_hitomi.setGeometry(QRect(20, 90, 51, 51))
        self.btn_hitomi.setFont(font1)
        self.btn_hitomi.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_hitomi.setStyleSheet(u"QPushButton {\n"
"	\n"
"	image: url(:/images/Hitomi.png);\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(9, 57, 104);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	image: url(:/images/logo.png);\n"
"	background-color: rgb(12, 91, 171);\n"
"}\n"
"\n"
"\n"
"")
        self.txt_passcode = QLineEdit(self.groupBox)
        self.txt_passcode.setObjectName(u"txt_passcode")
        self.txt_passcode.setGeometry(QRect(80, 40, 201, 30))
        font3 = QFont()
        font3.setPointSize(10)
        self.txt_passcode.setFont(font3)
        self.txt_passcode.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,225);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px")
        self.btn_hgallery = QPushButton(self.groupBox)
        self.btn_hgallery.setObjectName(u"btn_hgallery")
        self.btn_hgallery.setGeometry(QRect(90, 90, 51, 51))
        self.btn_hgallery.setFont(font1)
        self.btn_hgallery.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_hgallery.setStyleSheet(u"QPushButton {\n"
"	\n"
"	\n"
"	image: url(:/images/MHG.PNG);\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(9, 57, 104);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	image: url(:/images/logo.png);\n"
"	background-color: rgb(12, 91, 171);\n"
"}\n"
"\n"
"\n"
"")
        self.btn_hgif = QPushButton(self.groupBox)
        self.btn_hgif.setObjectName(u"btn_hgif")
        self.btn_hgif.setGeometry(QRect(160, 90, 51, 51))
        self.btn_hgif.setFont(font1)
        self.btn_hgif.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_hgif.setStyleSheet(u"QPushButton {\n"
"	\n"
"	image: url(:/images/Hgif.png);\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	image: url(:/images/logo.png);\n"
"	background-color: rgb(12, 91, 171);\n"
"}\n"
"\n"
"\n"
"")
        self.btn_ehen = QPushButton(self.groupBox)
        self.btn_ehen.setObjectName(u"btn_ehen")
        self.btn_ehen.setGeometry(QRect(230, 90, 51, 51))
        self.btn_ehen.setFont(font1)
        self.btn_ehen.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ehen.setStyleSheet(u"QPushButton {\n"
"	\n"
"	image: url(:/images/EHG.png);\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(9, 57, 104);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	image: url(:/images/logo.png);\n"
"	background-color: rgb(12, 91, 171);\n"
"}\n"
"\n"
"\n"
"")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(30, 310, 301, 101))
        self.groupBox_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_hanime = QPushButton(self.groupBox_2)
        self.btn_hanime.setObjectName(u"btn_hanime")
        self.btn_hanime.setGeometry(QRect(20, 30, 51, 51))
        self.btn_hanime.setFont(font1)
        self.btn_hanime.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_hanime.setStyleSheet(u"QPushButton {\n"
"	\n"
"	image: url(:/images/hanime.png);\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0,0,0);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	image: url(:/images/logo.png);\n"
"	background-color: rgb(12, 91, 171);\n"
"}\n"
"\n"
"\n"
"")
        self.btn_hworld = QPushButton(self.groupBox_2)
        self.btn_hworld.setObjectName(u"btn_hworld")
        self.btn_hworld.setGeometry(QRect(160, 30, 51, 51))
        self.btn_hworld.setFont(font1)
        self.btn_hworld.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_hworld.setStyleSheet(u"QPushButton {\n"
"	\n"
"	\n"
"	image: url(:/images/hworld.PNG);\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0,0,0);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	image: url(:/images/logo.png);\n"
"	background-color: rgb(12, 91, 171);\n"
"}\n"
"\n"
"\n"
"")
        self.btn_henhav = QPushButton(self.groupBox_2)
        self.btn_henhav.setObjectName(u"btn_henhav")
        self.btn_henhav.setGeometry(QRect(90, 30, 51, 51))
        self.btn_henhav.setFont(font1)
        self.btn_henhav.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_henhav.setStyleSheet(u"QPushButton {\n"
"	\n"
"	image: url(:/images/HH.PNG);\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0,0,0);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	image: url(:/images/logo.png);\n"
"	background-color: rgb(12, 91, 171);\n"
"}\n"
"\n"
"\n"
"")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(30, 420, 301, 101))
        self.groupBox_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_hgame = QPushButton(self.groupBox_3)
        self.btn_hgame.setObjectName(u"btn_hgame")
        self.btn_hgame.setGeometry(QRect(20, 30, 51, 51))
        self.btn_hgame.setFont(font1)
        self.btn_hgame.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_hgame.setStyleSheet(u"QPushButton {\n"
"	\n"
"	image: url(:/images/game.jpg);\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0,0,0);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	image: url(:/images/logo.png);\n"
"	background-color: rgb(12, 91, 171);\n"
"}\n"
"\n"
"\n"
"")
        self.btn_fnation = QPushButton(self.groupBox_3)
        self.btn_fnation.setObjectName(u"btn_fnation")
        self.btn_fnation.setGeometry(QRect(90, 30, 51, 51))
        self.btn_fnation.setFont(font1)
        self.btn_fnation.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_fnation.setStyleSheet(u"QPushButton {\n"
"	image: url(:/images/game.jpg);\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0,0,0);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	image: url(:/images/logo.png);\n"
"	background-color: rgb(12, 91, 171);\n"
"}\n"
"\n"
"\n"
"")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 700, 91, 20))
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.btn_color = QPushButton(self.centralwidget)
        self.btn_color.setObjectName(u"btn_color")
        self.btn_color.setGeometry(QRect(300, 700, 41, 21))
        font4 = QFont()
        font4.setPointSize(7)
        font4.setBold(True)
        self.btn_color.setFont(font4)
        self.btn_color.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_color.setStyleSheet(u"QPushButton {\n"
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
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(30, 530, 301, 161))
        self.groupBox_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_jav1 = QPushButton(self.groupBox_4)
        self.btn_jav1.setObjectName(u"btn_jav1")
        self.btn_jav1.setGeometry(QRect(20, 30, 51, 51))
        self.btn_jav1.setFont(font1)
        self.btn_jav1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_jav1.setStyleSheet(u"QPushButton {\n"
"	\n"
"	image: url(:/images/logo.png);\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0,0,0);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	image: url(:/images/logo.png);\n"
"	background-color: rgb(12, 91, 171);\n"
"}\n"
"\n"
"\n"
"")
        self.btn_jav2 = QPushButton(self.groupBox_4)
        self.btn_jav2.setObjectName(u"btn_jav2")
        self.btn_jav2.setGeometry(QRect(90, 30, 51, 51))
        self.btn_jav2.setFont(font1)
        self.btn_jav2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_jav2.setStyleSheet(u"QPushButton {\n"
"	\n"
"	image: url(:/images/logo.png);\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0,0,0);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	image: url(:/images/logo.png);\n"
"	background-color: rgb(12, 91, 171);\n"
"}\n"
"\n"
"\n"
"")
        self.btn_jav3 = QPushButton(self.groupBox_4)
        self.btn_jav3.setObjectName(u"btn_jav3")
        self.btn_jav3.setGeometry(QRect(160, 30, 51, 51))
        self.btn_jav3.setFont(font1)
        self.btn_jav3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_jav3.setStyleSheet(u"QPushButton {\n"
"	\n"
"	image: url(:/images/logo.png);\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0,0,0);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	image: url(:/images/logo.png);\n"
"	background-color: rgb(12, 91, 171);\n"
"}\n"
"\n"
"\n"
"")
        self.btn_jav4 = QPushButton(self.groupBox_4)
        self.btn_jav4.setObjectName(u"btn_jav4")
        self.btn_jav4.setGeometry(QRect(230, 30, 51, 51))
        self.btn_jav4.setFont(font1)
        self.btn_jav4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_jav4.setStyleSheet(u"QPushButton {\n"
"	\n"
"	image: url(:/images/logo.png);\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0,0,0);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	image: url(:/images/logo.png);\n"
"	background-color: rgb(12, 91, 171);\n"
"}\n"
"\n"
"\n"
"")
        self.btn_jav5 = QPushButton(self.groupBox_4)
        self.btn_jav5.setObjectName(u"btn_jav5")
        self.btn_jav5.setGeometry(QRect(20, 90, 51, 51))
        self.btn_jav5.setFont(font1)
        self.btn_jav5.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_jav5.setStyleSheet(u"QPushButton {\n"
"	\n"
"	image: url(:/images/logo.png);\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0,0,0);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	image: url(:/images/logo.png);\n"
"	background-color: rgb(12, 91, 171);\n"
"}\n"
"\n"
"\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText("")
        self.btn_minimize.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.logo_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">NBrowser Dashboard</span></p></body></html>", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Doujinshi", None))
        self.btn_nhentai.setText("")
        self.btn_hitomi.setText("")
        self.txt_passcode.setText("")
        self.txt_passcode.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Hentai Code Sauce", None))
        self.btn_hgallery.setText("")
        self.btn_hgif.setText("")
        self.btn_ehen.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Hentai Videos", None))
        self.btn_hanime.setText("")
        self.btn_hworld.setText("")
        self.btn_henhav.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Eroge VN Games", None))
        self.btn_hgame.setText("")
        self.btn_fnation.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Version 1.0.0</span></p></body></html>", None))
        self.btn_color.setText(QCoreApplication.translate("MainWindow", u"dawn", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"JAV", None))
        self.btn_jav1.setText("")
        self.btn_jav2.setText("")
        self.btn_jav3.setText("")
        self.btn_jav4.setText("")
        self.btn_jav5.setText("")
    # retranslateUi

