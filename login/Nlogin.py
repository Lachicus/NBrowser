import sys
import os.path
import json

## Warning, Info & Help Messages
import tkinter as tk

root = tk.Tk()
root.withdraw()
from tkinter import messagebox
root.iconbitmap('logo.ico')
## UI classes

from PySide6.QtWidgets import QTableWidget, QApplication, QMainWindow
from login.loginwindow import Ui_MainWindow


from browser.Nbrowser import Nbrowserview

class LoginWindow(QMainWindow):
    def __init__(self):
        ## MENU INSTANCES
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## BUTTON INTERACTABLES
        self.ui.pushButton.clicked.connect(lambda: self.authenticate())
        self.ui.btn_exit.clicked.connect(lambda: self.exitwindow())

        ## SHOW
        self.show()

    def authenticate(self):
        try:
            directory = "System69"
            parent_dir = os.getenv('APPDATA')
            path = os.path.join(parent_dir, directory)
            f = open(f"{path}\data.json")
            data = json.load(f)

            saved_code = data['passcode']
            code = self.ui.txt_passcode.text()

            if (saved_code == code):
                messagebox.showwarning("Login Success", "Welcome to NBrowser")
                self.main = Nbrowserview()
                self.main.show()
                self.close()
            if (saved_code != code):
                self.ui.label_5.setText("Passcode is Incorrect: Try Again")

        except:
            pass

    def exitwindow(self):
        response = messagebox.askquestion("Exit","Are you sure you want to stop using NBrowser?")
        if response == "yes":
            sys.exit(self)