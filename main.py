import csv
import re

from PyQt5 import QtWidgets, QtCore

from GUI import Ui_MainWindow

import Register
import favourite
import Warning
import About
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

        # Favourite window
        self.favourite_window = QtWidgets.QDialog()
        self.favourite_obj = favourite.Ui_Dialog()
        self.favourite_obj.setupUi(self.favourite_window)

        # Warning window
        self.warning_window = QtWidgets.QDialog()
        self.warning_obj = Warning.Ui_Dialog()
        self.warning_obj.setupUi(self.warning_window)

        # About window
        self.about_window = QtWidgets.QDialog()
        self.about_obj = About.Ui_Dialog()
        self.about_obj.setupUi(self.about_window)

        # Buttons connection
        self.main_obj.pushButton_2.clicked.connect(lambda: self.register_window.show())
        self.main_obj.pushButton.clicked.connect(self.login)
        self.register_obj.pushButton.clicked.connect(self.register)
        self.main_obj.pushButton_3.clicked.connect(self.move_back)
        self.main_obj.pushButton_6.clicked.connect(
            lambda: self.main_obj.stackedWidget.setCurrentWidget(self.main_obj.page_2))
        self.main_obj.pushButton_7.clicked.connect(lambda: self.about_window.show())
        self.main_obj.pushButton_5.clicked.connect(
            lambda: self.main_obj.stackedWidget.setCurrentWidget(self.main_obj.login_page))
        self.main_obj.pushButton_8.clicked.connect(self.favourite_window_show)
        self.main_obj.pushButton_10.clicked.connect(self.logout)
        self.main_obj.pushButton_9.clicked.connect(self.add_to_favourite)
        self.favourite_obj.pushButton_2.clicked.connect(self.favourite_item_clicked)
        self.favourite_obj.pushButton.clicked.connect(self.delete_favourite_item)

        # link the list of restaurants with the function
        self.main_obj.listWidget.itemClicked.connect(self.list_item_clicked)

        # If any item selected in the combo box
        self.main_obj.pushButton_4.clicked.connect(self.combo_value_changed)

        # Start the window with login page
        self.main_obj.stackedWidget.setCurrentWidget(self.main_obj.login_page)

        # Initially the login is appear
        self.main_obj.frame_4.setVisible(True)
        self.main_obj.frame_8.setVisible(False)

        # Load the dataset
        self.df = pd.read_csv("data/zomato.csv", encoding="ISO-8859-1")

        # Clean the data frame
        self.df = self.clean_data(self.df.astype(str))

        # Question
        self.Features = ['City', 'Cuisines', 'Has_Online_delivery', 'Has_Table_booking', 'Average_Cost_for_two',
                         'Currency']

        # start with First Feature
        self.column = 0
    def delete_favourite_item(self):

        members = self.favourite_obj.listWidget.currentItem()
        row = self.favourite_obj.listWidget.row(members)
        self.favourite_obj.listWidget.takeItem(row)

        lines = list()
        with open('data/favourite.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == members:
                        lines.remove(row)
        with open('data/favourite.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

    def favourite_item_clicked(self):
        res = pd.read_csv('data/zomato.csv', encoding="ISO-8859-1")
        p = self.favourite_obj.listWidget.currentItem().text()
        record = res[res['Restaurant_Name'] == p]

        self.main_obj.label_5.setText("Restaurant name: " + p)
        self.main_obj.label_6.setText("Restaurant ID: " + str(record['Restaurant_ID'].values[0]))
        self.main_obj.label_11.setText("Cuisines: " + str(record['Cuisines'].values[0]))
        self.main_obj.label_12.setText("Currency: " + record['Currency'].values[0])
        self.main_obj.label_8.setText("City: " + record['City'].values[0])
        self.main_obj.label_10.setText("Locality: " + record['Locality'].values[0])
        self.main_obj.label_7.setText("Address: " + record['Address'].values[0])
        latitude = record['Latitude'].values[0]
        longitude = record['Longitude'].values[0]

        self.main_obj.webEngineView.setUrl(
            QtCore.QUrl("https://www.google.com/maps/place/" + str(latitude) + "," + str(longitude)))

        self.main_obj.stackedWidget.setCurrentWidget(self.main_obj.page)
        self.main_obj.pushButton_9.setEnabled(False)
        self.main_obj.listWidget.clear()
        self.favourite_window.close()

    def favourite_window_show(self):
        self.favourite_obj.listWidget.clear()
        res = pd.read_csv("data/favourite.csv")
        res_names = res['restaurant'].values
        self.favourite_obj.listWidget.addItems(res_names)
        self.favourite_window.show()

    def add_to_favourite(self):
        restaurant = self.main_obj.listWidget.currentItem().text()
        print(restaurant)
        res = pd.read_csv("data/favourite.csv").values
        if restaurant in res:
            self.warning_obj.label_2.setText("Restaurant already added")
            self.warning_window.show()
            return

        # create a new user entry
        row = [restaurant]
        with open("data/favourite.csv", "a") as f:
            wo = csv.writer(f, lineterminator='\n')
            wo.writerow(row)
            f.close()

    def logout(self):
        self.main_obj.frame_8.setVisible(False)
        self.main_obj.frame_4.setVisible(True)
        self.main_obj.lineEdit.setText("")
        self.main_obj.lineEdit_2.setText("")

    def move_back(self):
        self.main_obj.pushButton_9.setEnabled(True)
        # Load the dataset
        self.df = pd.read_csv("data/zomato.csv", encoding="ISO-8859-1")

        # Clean the data frame
        self.df = self.clean_data(self.df.astype(str))

        # start with First Feature
        self.column = 0

        # Go back to the selection screen
        self.main_obj.stackedWidget.setCurrentWidget(self.main_obj.page_2)

        # Reset the item of combo with cities
        cities = ['Birmingham', 'London', 'Manchester', 'Edinburgh', 'New Delhi', 'Mumbai', 'Dubai', 'Athens']
        self.main_obj.comboBox.clear()
        self.main_obj.comboBox.addItems(cities)
        self.main_obj.label_4.setText('City')

    def list_item_clicked(self):
        p = self.main_obj.listWidget.currentItem().text()
        self.main_obj.label_5.setText("Restaurant name: " + p)
        self.main_obj.label_6.setText(
            "Restaurant ID: " + self.df[self.df['Restaurant_Name'] == p]['Restaurant_ID'].values[0])
        self.main_obj.label_11.setText("Cuisines: " + self.df[self.df['Restaurant_Name'] == p]['Cuisines'].values[0])
        self.main_obj.label_12.setText("Currency: " + self.df[self.df['Restaurant_Name'] == p]['Currency'].values[0])
        self.main_obj.label_8.setText("City: " + self.df[self.df['Restaurant_Name'] == p]['City'].values[0])
        self.main_obj.label_10.setText("Locality: " + self.df[self.df['Restaurant_Name'] == p]['Locality'].values[0])
        self.main_obj.label_7.setText("Address: " + self.df[self.df['Restaurant_Name'] == p]['Address'].values[0])
        latitude = self.df[self.df['Restaurant_Name'] == p]['Latitude'].values[0]
        longitude = self.df[self.df['Restaurant_Name'] == p]['Longitude'].values[0]

        self.main_obj.webEngineView.setUrl(
            QtCore.QUrl("https://www.google.com/maps/place/" + str(latitude) + "," + str(longitude)))

    def combo_value_changed(self):
        # get the text from the combo
        text = self.main_obj.comboBox.currentText()
        # extract the df matching with Feature
        self.df = self.df[self.df[self.Features[self.column]] == text]

        # move to next column
        self.column += 1
        self.main_obj.comboBox.clear()
        self.main_obj.label_4.setText(self.Features[self.column])
        options = list(self.df[self.Features[self.column]].unique())
        print(options)

        if len(options) == 1:
            self.main_obj.stackedWidget.setCurrentWidget(self.main_obj.page)
            self.main_obj.listWidget.clear()
            self.main_obj.listWidget.addItems(self.df['Restaurant_Name'].unique())
            return

        self.main_obj.comboBox.addItems(options)

    def clean_data(self, dataset):
        cols = dataset.columns
        data = dataset[cols].values.flatten()

        s = pd.Series(data)
        s = s.str.strip()
        s = s.values.reshape(dataset.shape)

        dataset = pd.DataFrame(s, columns=dataset.columns)

        return dataset.astype(str)

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
            self.main_obj.frame_4.setVisible(False)
            self.main_obj.frame_8.setVisible(True)
        else:
            self.warning_obj.label_2.setText("Wrong email or password")
            self.warning_window.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    ui.main_window.show()
    sys.exit(app.exec_())
