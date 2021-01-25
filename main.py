import csv
import re

from PyQt5 import QtWidgets

from GUI import Ui_MainWindow

import Register
import Warning
import pandas as pd


class Main:

    def __init__(self):
        # Main_window
        self.main_window = QtWidgets.QMainWindow()
        self.main_obj = Ui_MainWindow()
        self.main_obj.setupUi(self.main_window)

        # Signup window
        self.register_window = QtWidgets.QDialog()
        self.register_obj = Register.Ui_Dialog()
        self.register_obj.setupUi(self.register_window)

        # Warning window
        self.warning_window = QtWidgets.QDialog()
        self.warning_obj = Warning.Ui_Dialog()
        self.warning_obj.setupUi(self.warning_window)

        # Buttons connection
        self.main_obj.pushButton_2.clicked.connect(lambda: self.register_window.show())
        self.main_obj.pushButton.clicked.connect(self.login)
        self.register_obj.pushButton.clicked.connect(self.register)

    def encode(self, password):
        encode = ""
        for i in password:
            encode = encode + chr(ord(i) + 18)
        return encode

    def decode(self, password):
        decode = ""
        for i in password:
            decode = decode + chr(ord(i) - 18)
        return decode

    def user_exists(self, email):
        users = pd.read_csv("data/users.csv")
        for i in users['email']:
            if i == email:
                return True
        return False

    def check_user(self, email, password):
        users = pd.read_csv("data/users.csv")
        for i in users['email']:
            if i == email:
                password = self.encode(password)
                if users[users['email'] == i]['password'].values[0] == password:
                    return True
        return False

    def check_valid_email(self, email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        # pass the regular expression
        # and the string in search() method
        if re.search(regex, email):
            return True
        else:
            return False

    def register(self):
        email = self.register_obj.lineEdit.text()
        password = self.register_obj.lineEdit_2.text()
        confirm_password = self.register_obj.lineEdit_3.text()

        if email is "" or password is "" or confirm_password is "":
            self.warning_obj.label_2.setText("Please fill all the field")
            self.warning_window.show()
            return
        elif not self.check_valid_email(email):
            self.warning_obj.label_2.setText("Email is not valid")
            self.warning_window.show()
            return
        elif password != confirm_password:
            self.warning_obj.label_2.setText("Passwords don't matched")
            self.warning_window.show()
            return

        elif self.user_exists(email):
            self.warning_obj.label_2.setText("User already exists")
            self.warning_window.show()
            return

        password = self.encode(password)

        # create a new user entry
        row = [email, password]
        with open("data/users.csv", "a") as f:
            wo = csv.writer(f, lineterminator='\n')
            wo.writerow(row)

        self.register_window.destroy()

    def login(self):
        input_email = self.main_obj.lineEdit.text()
        input_password = self.main_obj.lineEdit_2.text()

        if self.check_user(input_email, input_password):
            self.main_obj.stackedWidget.setCurrentWidget(self.main_obj.page_2)
        else:
            self.warning_obj.label_2.setText("Wrong email or password")
            self.warning_window.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    ui.main_window.show()
    sys.exit(app.exec_())
