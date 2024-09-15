import sys
import os.path
import json

## Warning, Info & Help Messages
import tkinter as tk

from browser.Ninstance import Nwindow

root = tk.Tk()
root.withdraw()
from tkinter import messagebox
root.iconbitmap('logo.ico')

## UI classes
import PySide6
from browser.Ndashboard import Ui_MainWindow
from PySide6.QtWidgets import QTableWidget, QApplication, QMainWindow
from PySide6.QtCore import Qt, QPoint
from browser.Ninstancewindow import Ui_Instance

## Globals
UI_Theme = "Dusk"


class Nbrowserview(QMainWindow):
    def __init__(self):
        ## MENU INSTANCES
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        test = Ui_Instance()


        ## THEMES
        directory = "System69"
        parent_dir = os.getenv('APPDATA')
        path = os.path.join(parent_dir, directory)
        f = open(f"{path}\data.json")
        data = json.load(f)
        global UI_Theme

        bg_color = data['theme']
        UI_Theme = data['themeMode']

        self.ui.label_4.setStyleSheet(
            f"{bg_color}\n"
            "border-radius:8px;"
        )

        ## BUTTONS
        self.ui.btn_exit.clicked.connect(lambda: self.close())
        self.ui.btn_minimize.clicked.connect(lambda: self.minimize())
        self.ui.btn_color.clicked.connect(lambda: self.theme(test))
        self.ui.btn_nhentai.clicked.connect(lambda: self.nhentai())
        self.ui.btn_hitomi.clicked.connect(lambda: self.hitomi())

    # Mouse Events
    def mousePressEvent(self, event:PySide6.QtGui.QMouseEvent):
        self.oldPosition = event.globalPos()

        print()
    def mouseMoveEvent(self, event:PySide6.QtGui.QMouseEvent):
        delta = QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()

    # Taskbar Events
    def close(self):
        response = messagebox.askquestion("Exit", "Are you sure you want to stop using NBrowser?")
        if response == "yes":
            sys.exit(self)

    def minimize(self):
        self.showMinimized()

    # Themes
    def theme(self,test):
        global UI_Theme

        if UI_Theme == "Dusk":
            directory = "System69"
            parent_dir = os.getenv('APPDATA')
            path = os.path.join(parent_dir, directory)
            f = open(f"{path}\data.json")
            data = json.load(f)

            data['theme'] = 'background-color:rgba(36, 22, 105, 225);'
            data['themeMode'] = 'Dawn'
            UI_Theme = 'Dawn'

            with open(f"{path}\data.json", "w") as outfile:
                json.dump(data, outfile)

            self.ui.label_4.setStyleSheet(
                f"background-color:rgba(36, 22, 105, 225);\n"
                "border-radius:8px;"
            )

            self.ui.btn_color.setText("Dusk")
            return


        if UI_Theme == "Dawn":
            directory = "System69"
            parent_dir = os.getenv('APPDATA')
            path = os.path.join(parent_dir, directory)
            f = open(f"{path}\data.json")
            data = json.load(f)

            data['theme'] = 'background-color:rgba(6, 1, 28, 225);'
            data['themeMode'] = 'Dusk'
            UI_Theme = 'Dusk'

            with open(f"{path}\data.json", "w") as outfile:
                json.dump(data, outfile)

            self.ui.label_4.setStyleSheet(
                f"background-color:rgba(6, 1, 28, 225);\n"
                "border-radius:8px;"
            )

            self.ui.btn_color.setText("Dawn")
            return



    # Doujinshi
    def nhentai(self):
        messagebox.showwarning("Nhentai", "Welcome to Nhentai")
        code = self.ui.txt_passcode.text()
        if code == "":
            self.main = Nwindow("https://nhentai.net/","Nhentai")
        else:
            self.main = Nwindow(f"https://nhentai.net/g/{code}", "Nhentai")
        self.main.show()

    def hitomi(self):
        messagebox.showwarning("Nhentai", "Welcome to Hitomi")
        self.main = Nwindow("https://hitomi.la/", "Hitomi")
        self.main.show()