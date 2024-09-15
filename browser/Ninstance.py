import sys
from tkinter import messagebox

import PySide6
from PySide6.QtWidgets import QMainWindow
from browser.Ninstancewindow import Ui_Instance
from PySide6.QtWebEngineWidgets import *
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Nwindow(QMainWindow):
    def __init__(self,Url,Title,):
        ## MENU INSTANCES
        QMainWindow.__init__(self)
        self.ui = Ui_Instance()
        self.ui.setupUi(self)
        self.window().setWindowTitle(Title)

        ## BROWSER
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(Url))
        self.ui.webcasing.addWidget(self.browser)
        self.browser.setZoomFactor(0.75)

        ## BUTTONS
        self.ui.btn_exit.clicked.connect(lambda: self.exit())
        self.ui.btn_minimize.clicked.connect(lambda: self.minimize())


    # Mouse Events
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent):
        self.oldPosition = event.globalPos()


    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent):
        delta = QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()

    # Buttons

    # Taskbar Events
    def exit(self):
        response = messagebox.askquestion("Exit", "Are you sure you want to stop using NBrowser?")
        if response == "yes":
            self.close()

    def minimize(self):
        self.showMinimized()