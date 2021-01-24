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

    def check_user(self, email, password):
        users = pd.read_csv("data/users.csv")
        for i in users['email']:
            if i == email:
                if users[users['email'] == i]['password'] == password:
                    return True
        return False

    def register(self):
        pass

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
