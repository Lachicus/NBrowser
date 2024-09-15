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
from PySide6.QtWidgets import QApplication, QMainWindow
from login.Nlogin import LoginWindow
from register.Nregister import RegistrationWindow


## Initialize system folders and resources
try:
    directory = "System69"
    parent_dir = os.getenv('APPDATA')
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
except: pass

## Global Variables
registration = False


## Access appdata json
try:
    directory = "System69"
    parent_dir = os.getenv('APPDATA')
    path = os.path.join(parent_dir, directory)
    f = open(f"{path}\data.json")
    data = json.load(f)

    registration = data['registration']

except: pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    if registration:
        window = LoginWindow()
    else:
        window = RegistrationWindow()
    sys.exit(app.exec())