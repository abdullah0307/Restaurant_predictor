import csv
import os
import re

import cv2
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog

from GUI import Ui_MainWindow

import Register
import favourite
import Warning
import About
import Profile
import pandas as pd


class Main:

    def __init__(self):

        # User values
        self.user_name = ""
        self.user_email = ""
        self.user_password = ""
        self.user_image = ""
        self.user_language = ""
        self.user_role = ""
        self.user_gender = ""
        self.user_country = ""

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

        # Profile window
        self.profile_window = QtWidgets.QDialog()
        self.profile_obj = Profile.Ui_Dialog()
        self.profile_obj.setupUi(self.profile_window)

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
        self.main_obj.pushButton_11.clicked.connect(self.show_profile_window)
        self.main_obj.lineEdit_3.textChanged.connect(self.search_bar_text_change)
        self.main_obj.listWidget_2.itemDoubleClicked.connect(self.search_list_item_clicked)
        self.main_obj.pushButton_15.clicked.connect(self.show_all_restaurants)
        self.main_obj.pushButton_13.clicked.connect(self.open_contact_us)
        self.main_obj.pushButton_14.clicked.connect(self.submit_query)
        self.main_obj.pushButton_16.clicked.connect(lambda: self.main_obj.stackedWidget.setCurrentWidget(self.main_obj.login_page))
        self.main_obj.push

        # Favourite window buttons
        self.favourite_obj.pushButton_2.clicked.connect(self.favourite_item_clicked)
        self.favourite_obj.pushButton.clicked.connect(self.delete_favourite_item)

        self.register_obj.pushButton_2.clicked.connect(self.get_user_image)
        self.main_obj.pushButton_12.clicked.connect(self.show_profile_window)

        # Any changing in the profile change
        self.profile_obj.lineEdit.textChanged.connect(self.line_edit_change)
        self.profile_obj.lineEdit_2.textChanged.connect(self.line_edit_change)
        self.profile_obj.lineEdit_4.textChanged.connect(self.line_edit_change)
        self.profile_obj.lineEdit_5.textChanged.connect(self.line_edit_change)
        self.profile_obj.radioButton_3.clicked.connect(self.line_edit_change)
        self.profile_obj.radioButton_2.clicked.connect(self.line_edit_change)
        self.profile_obj.radioButton_4.clicked.connect(self.line_edit_change)
        self.profile_obj.radioButton.clicked.connect(self.line_edit_change)
        self.profile_obj.pushButton_2.clicked.connect(self.profile_image_update)

        # link the list of restaurants with the function
        self.main_obj.listWidget.itemClicked.connect(self.list_item_clicked)

        # If any item selected in the combo box
        self.main_obj.pushButton_4.clicked.connect(self.combo_value_changed)

        # Start the window with login page
        self.main_obj.stackedWidget.setCurrentWidget(self.main_obj.login_page)

        # Save Changes
        self.profile_obj.pushButton.clicked.connect(self.save_changes)

        # Initially the login is appear
        self.main_obj.frame_4.setVisible(True)
        self.main_obj.frame_8.setVisible(False)

        # User label is not visible
        self.main_obj.label.setVisible(True)
        self.main_obj.pushButton_2.setVisible(True)
        self.main_obj.label_19.setVisible(False)
        self.main_obj.pushButton_12.setVisible(False)

        # Load the dataset
        self.df = pd.read_csv("data/zomato.csv", encoding="ISO-8859-1")

        # Clean the data frame
        self.df = self.clean_data(self.df.astype(str))

        # Question
        self.Features = ['City', 'Cuisines', 'Has_Online_delivery', 'Has_Table_booking', 'Average_Cost_for_two',
                         'Currency']

        # start with First Feature
        self.column = 0

        # initially the search list is invisible
        self.main_obj.listWidget_2.setVisible(False)

        # Users data
        self.restaurants = pd.read_csv("data/zomato.csv", encoding="ISO-8859-1")

    def submit_query(self):
        if self.main_obj.lineEdit_4.text() is "" or self.main_obj.lineEdit_5 is "" or self.main_obj.lineEdit_6 is "" or self.main_obj.lineEdit_7 is "":
            self.warning_obj.label_2.setText("please fill all the fields")
            self.warning_window.show()
            return

        if not self.check_valid_email(self.main_obj.lineEdit_7.text()):
            self.warning_obj.label_2.setText("Email is not valid")
            self.warning_window.show()
            return

        first_name = self.main_obj.lineEdit_4.text()
        last_name = self.main_obj.lineEdit_6.text()
        email = self.main_obj.lineEdit_7.text()
        phone_number = self.main_obj.lineEdit_5.text()
        queries = self.main_obj.textEdit.toPlainText()

        record = [first_name, last_name, email, phone_number, queries]
        file_name = "data/queries.csv"
        # Open file in append mode
        with open(file_name, 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = csv.writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow(record)

        self.main_obj.stackedWidget.setCurrentWidget(self.main_obj.login_page)


    def open_contact_us(self):
        self.main_obj.textEdit.setText("")
        self.main_obj.lineEdit_4.setText("")
        self.main_obj.lineEdit_5.setText("")
        self.main_obj.lineEdit_6.setText("")
        self.main_obj.lineEdit_7.setText("")
        # Navigate to contact us form
        self.main_obj.stackedWidget.setCurrentWidget(self.main_obj.Contact_us)

    def show_all_restaurants(self):
        res = pd.read_csv('data/zomato.csv', encoding="ISO-8859-1")
        records = res['Restaurant_Name'].values
        self.main_obj.listWidget.clear()
        self.main_obj.listWidget.addItems(records)

        self.main_obj.label_5.setText("Restaurant name: ")
        self.main_obj.label_6.setText("Restaurant ID: ")
        self.main_obj.label_11.setText("Cuisines: ")
        self.main_obj.label_12.setText("Currency: ")
        self.main_obj.label_8.setText("City: ")
        self.main_obj.label_10.setText("Locality: ")
        self.main_obj.label_7.setText("Address: ")

        self.main_obj.webEngineView.setUrl(
            QtCore.QUrl(""))

        self.main_obj.stackedWidget.setCurrentWidget(self.main_obj.page)
        self.main_obj.pushButton_9.setEnabled(True)

    def search_list_item_clicked(self):
        res = pd.read_csv('data/zomato.csv', encoding="ISO-8859-1")
        p = self.main_obj.listWidget_2.currentItem().text()
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

    def check_restaurant(self, res):
        restaurants = self.restaurants[self.restaurants["Restaurant_Name"].str.contains(res)]['Restaurant_Name']
        return restaurants

    def search_bar_text_change(self):
        if self.main_obj.lineEdit_3.text() is "":
            self.main_obj.listWidget_2.setVisible(False)
        else:
            self.main_obj.listWidget_2.setVisible(True)
            self.main_obj.listWidget_2.clear()
            self.main_obj.listWidget_2.addItems(self.check_restaurant(self.main_obj.lineEdit_3.text()))

    def profile_image_update(self):
        # open the dialogue box to select the file
        options = QtWidgets.QFileDialog.Options()

        # Show input file dialogue
        path = QFileDialog.getOpenFileName(caption="Select image", directory="",
                                           filter="Jpg (*.jpg);;Jpeg (*.jpeg);;png (*.png);;All files (*.*)",
                                           options=options)

        # Set the image
        self.profile_obj.label_2.setPixmap(QtGui.QPixmap(path[0]))

        # Save user image path
        self.user_image = path[0]

    def check_profile_edits(self):
        if self.profile_obj.lineEdit.text() is "" or self.profile_obj.lineEdit_4.text() is "" or self.profile_obj.lineEdit_5.text() is "":
            return True
        else:
            return False

    def save_changes(self):
        # If fields are empty
        if self.check_profile_edits():
            return

        lines = list()
        new_row = [self.user_name, self.user_email, self.user_country, self.user_language, self.user_role,
                   self.user_gender, self.user_password]

        # Load the saved user data
        with open('data/users.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == self.user_email:
                        lines.remove(row)
                        lines.append(new_row)

        # Save the updated user.csv
        with open('data/users.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

        self.profile_window.close()

        self.warning_obj.label_2.setText("Changes Saved")
        self.warning_window.show()

    def line_edit_change(self):
        self.user_name = self.profile_obj.lineEdit.text()
        self.user_language = self.profile_obj.lineEdit_5.text()
        self.user_country = self.profile_obj.lineEdit_4.text()

        if self.profile_obj.radioButton_2.isChecked():
            self.user_gender = "Male"
        else:
            self.user_gender = "Female"

        if self.profile_obj.radioButton_3.isChecked():
            self.user_role = "Admin"
        else:
            self.user_role = "User"

        # Setting up the user data
        self.profile_obj.label_3.setText("Name: " + self.user_name)
        self.profile_obj.label_5.setText("Role: " + self.user_role)
        self.profile_obj.label_16.setText("Gender: " + self.user_gender)
        self.profile_obj.label_11.setText("Country: " + self.user_country)
        self.profile_obj.label_12.setText("Language:" + self.user_language)

    def get_user_image(self):
        # open the dialogue box to select the file
        options = QtWidgets.QFileDialog.Options()

        # Show input file dialogue
        path = QFileDialog.getOpenFileName(caption="Select image", directory="",
                                           filter="Jpg (*.jpg);;Jpeg (*.jpeg);;png (*.png);;All files (*.*)",
                                           options=options)

        # Set the image
        self.register_obj.label_10.setPixmap(QtGui.QPixmap(path[0]))

        # Save user image path
        self.user_image = path[0]

    def show_profile_window(self):

        # Setting up the user data
        self.profile_obj.label_3.setText("Name: " + self.user_name)
        self.profile_obj.label_4.setText("Email: " + self.user_email)
        self.profile_obj.label_5.setText("Role: " + self.user_role)
        self.profile_obj.label_16.setText("Gender: " + self.user_gender)
        self.profile_obj.label_11.setText("Country: " + self.user_country)
        self.profile_obj.label_12.setText("Language:" + self.user_language)

        # Email show in line edit disabled
        self.profile_obj.lineEdit_2.setText(self.user_email)

        if self.user_gender == 'Male':
            self.profile_obj.radioButton_2.setChecked(True)
        else:
            self.profile_obj.radioButton.setChecked(True)

        if self.user_role == 'Admin':
            self.profile_obj.radioButton_3.setChecked(True)
        else:
            self.profile_obj.radioButton_4.setChecked(True)

        if os.path.exists("data/User images/" + self.user_name + ".jpg"):
            self.profile_obj.label_2.setPixmap(QtGui.QPixmap("data/User images/" + self.user_name + ".jpg"))
        else:
            self.profile_obj.label_2.setPixmap(QtGui.QPixmap("images/avatar.jpeg"))

        # Show the profile window
        self.profile_window.show()

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
        self.main_obj.label.setVisible(True)
        self.main_obj.pushButton_2.setVisible(True)
        self.main_obj.label_19.setVisible(False)
        self.main_obj.pushButton_12.setVisible(False)

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

        # Get all the values from the form of register window
        user_name = self.register_obj.lineEdit_4.text()
        email = self.register_obj.lineEdit.text()
        country = self.register_obj.lineEdit_5.text()
        language = self.register_obj.lineEdit_6.text()
        role = self.register_obj.comboBox.currentText()
        if self.register_obj.radioButton.isChecked():
            gender = "Male"
        else:
            gender = "Female"
        password = self.register_obj.lineEdit_2.text()
        confirm_password = self.register_obj.lineEdit_3.text()

        # Check for all the fields are empty or not
        if email is "" or password is "" or confirm_password is "" or user_name is "" or country is "" or language is "" or role is "" or gender is "":
            self.warning_obj.label_2.setText("Please fill all the field")
            self.warning_window.show()
            return
        # Check for email is valid or not
        elif not self.check_valid_email(email):
            self.warning_obj.label_2.setText("Email is not valid")
            self.warning_window.show()
            return
        # Check for the password is matched with the confirm password
        elif password != confirm_password:
            self.warning_obj.label_2.setText("Passwords don't matched")
            self.warning_window.show()
            return
        # Check for the user exists or not
        elif self.user_exists(email):
            self.warning_obj.label_2.setText("User already exists")
            self.warning_window.show()
            return
        # Encrypt the password
        password = self.encode(password)

        # create a new user entry
        row = [user_name, email, country, language, role, gender, password]
        with open("data/users.csv", "a") as f:
            wo = csv.writer(f, lineterminator='\n')
            wo.writerow(row)

        print(self.user_image)
        # Save the user picture
        image = cv2.imread(self.user_image)
        cv2.imwrite("data/User images/" + user_name + ".jpg", image)

        # Finish the registration
        self.register_window.destroy()

        # Clear the form and image
        self.register_obj.lineEdit.clear()
        self.register_obj.lineEdit_2.clear()
        self.register_obj.lineEdit_3.clear()
        self.register_obj.lineEdit_4.clear()
        self.register_obj.lineEdit_5.clear()
        self.register_obj.lineEdit_6.clear()
        self.register_obj.label_10.setPixmap(QtGui.QPixmap("images/avatar.jpeg"))

    def login(self):
        input_email = self.main_obj.lineEdit.text()
        input_password = self.main_obj.lineEdit_2.text()
        users = pd.read_csv("data/users.csv")

        if self.check_user(input_email, input_password):
            self.main_obj.frame_4.setVisible(False)
            self.main_obj.frame_8.setVisible(True)
            self.main_obj.label.setVisible(False)
            self.main_obj.pushButton_2.setVisible(False)
            self.main_obj.label_19.setVisible(True)
            self.main_obj.pushButton_12.setVisible(True)

            # Load the user profile
            self.user_name = users[users['email'] == input_email]['user_name'].values[0]
            self.user_role = users[users['email'] == input_email]['role'].values[0]
            self.user_email = users[users['email'] == input_email]['email'].values[0]
            self.user_language = users[users['email'] == input_email]['language'].values[0]
            self.user_password = users[users['email'] == input_email]['password'].values[0]
            self.user_gender = users[users['email'] == input_email]['gender'].values[0]
            self.user_country = users[users['email'] == input_email]['country'].values[0]
            self.user_image = cv2.imread("data/User images/" + self.user_name + ".jpg")

            # Set the button name with username
            self.main_obj.pushButton_12.setText(self.user_name)
            self.main_obj.pushButton_11.setText(self.user_name)

            # if the image found in the directory
            if os.path.exists("data/User images/" + self.user_name + ".jpg"):
                self.main_obj.label_19.setPixmap(QtGui.QPixmap("data/User images/" + self.user_name + ".jpg"))
                self.main_obj.label_18.setPixmap(QtGui.QPixmap("data/User images/" + self.user_name + ".jpg"))
            else:
                self.main_obj.label_19.setPixmap(QtGui.QPixmap("images/avatar.jpeg"))
                self.main_obj.label_18.setPixmap(QtGui.QPixmap("images/avatar.jpeg"))


        else:
            self.warning_obj.label_2.setText("Wrong email or password")
            self.warning_window.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    ui.main_window.show()
    sys.exit(app.exec_())
