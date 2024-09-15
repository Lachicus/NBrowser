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
from register.regwindow import Ui_RegWindow
from login.Nlogin import LoginWindow


class RegistrationWindow(QMainWindow):
    def __init__(self):
        ## MENU INSTANCES
        QMainWindow.__init__(self)
        self.ui = Ui_RegWindow()
        self.ui.setupUi(self)

        ## BUTTON INTERACTABLES
        self.ui.pushButton.clicked.connect(lambda: self.register())
        self.ui.btn_exit.clicked.connect(lambda: self.exitwindow())

        ## SHOW
        self.show()

    def register(self):
        global registrationproc
        code = self.ui.txt_passcode.text()
        confirmation = self.ui.txt_passcode_2.text()
        if (not (code and code.strip())):
            messagebox.showwarning("Error Ocurred", "'Passcode' cannot be empty")
            return
        if (not (confirmation and confirmation.strip())):
            messagebox.showwarning("Error Ocurred", "'Confirm Passcode' cannot be empty")
            return
        if (not len(code) == 4):
            messagebox.showwarning("Input Error", "Passcode must be 4 digits")
            return
        if (code == confirmation):
            response = messagebox.askquestion("Confirmation", "Do you want to proceed to login? or change passcode?")
            if response == "yes":
                directory = "System69"
                parent_dir = os.getenv('APPDATA')
                path = os.path.join(parent_dir, directory)
                registerData = {
                    "passcode": f"{code}",
                    "registration": "True",
                    "theme": "background-color:rgba(6, 1, 28, 225);",
                    "themeMode": "Dusk"
                }
                with open(f"{path}\data.json", "w") as outfile:
                    json.dump(registerData, outfile)

                ## Proceeds to Login Window

                self.main = LoginWindow()
                self.main.show()
                self.close()

            if response == "no":
                self.ui.txt_passcode.setText("")
                self.ui.txt_passcode_2.setText("")

        else:
            messagebox.showwarning("Registration Error", "Confirm Passcode does not match with Passcode")

    def exitwindow(self):
        response = messagebox.askquestion("Cancel Registration?","Are you sure you want to quit?")
        if response == "yes":
            sys.exit(self)