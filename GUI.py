# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1095, 857)
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        MainWindow.setStyleSheet("background-image: url(:/bg/images/Tallest Restaurants in the World 7.jpg);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"background-size: cover;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background:None;")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.login_page = QtWidgets.QWidget()
        self.login_page.setObjectName("login_page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.login_page)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 0, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.login_page)
        self.frame.setMinimumSize(QtCore.QSize(300, 0))
        self.frame.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame.setStyleSheet("background:none;\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:1.546, fx:0.5, fy:0.5, stop:0 rgba(223, 149, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:30px;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background:none")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem4)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setStyleSheet("background:none;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("background:none")
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 2, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background:none;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_4.addWidget(self.lineEdit_2, 2, 0, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background:none;")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_4.addWidget(self.lineEdit, 0, 0, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{background:none;\n"
" border-radius:6px;\n"
" color:#030202;\n"
" padding-top:5px;\n"
" padding-bottom:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(181, 121, 0);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_4.addWidget(self.pushButton_2, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{background:none;\n"
" border-radius:6px;\n"
" color:#030202;\n"
" padding-top:5px;\n"
" padding-bottom:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(181, 121, 0);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background:none")
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.frame_8 = QtWidgets.QFrame(self.frame)
        self.frame_8.setStyleSheet("background:None;\n"
"border:none;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_6.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton{background:none;\n"
" border-radius:6px;\n"
" color:#030202;\n"
" padding-top:5px;\n"
" padding-bottom:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(181, 121, 0);\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 0, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_7.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton{background:none;\n"
" border-radius:6px;\n"
" color:#030202;\n"
" padding-top:5px;\n"
" padding-bottom:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(181, 121, 0);\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_2.addWidget(self.pushButton_7, 2, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton{background:none;\n"
" border-radius:6px;\n"
" color:#030202;\n"
" padding-top:5px;\n"
" padding-bottom:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(181, 121, 0);\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_2.addWidget(self.pushButton_8, 1, 0, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_10.setMaximumSize(QtCore.QSize(16777215, 16777210))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("QPushButton{background:none;\n"
" border-radius:6px;\n"
" color:#030202;\n"
" padding-top:5px;\n"
" padding-bottom:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(181, 121, 0);\n"
"}")
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_2.addWidget(self.pushButton_10, 3, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_8)
        self.gridLayout_3.addWidget(self.frame, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.login_page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setStyleSheet("background:None;")
        self.page_2.setObjectName("page_2")
        self.gridLayout = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 2, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 3, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 3, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 4, 1, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.page_2)
        self.frame_6.setMinimumSize(QtCore.QSize(500, 400))
        self.frame_6.setMaximumSize(QtCore.QSize(500, 400))
        self.frame_6.setStyleSheet("background:none;\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:1.546, fx:0.5, fy:0.5, stop:0 rgba(223, 149, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:30px;\n"
"")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem9)
        self.label_9 = QtWidgets.QLabel(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background:none")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background:none")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem10)
        self.comboBox = QtWidgets.QComboBox(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox.setFont(font)
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setStyleSheet("background:none")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem11)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton{background:none;\n"
" border-radius:6px;\n"
" color:#030202;\n"
" padding-top:5px;\n"
" padding-bottom:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(181, 121, 0);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.hboxlayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_5.setStyleSheet("QPushButton{background:none;\n"
" border-radius:6px;\n"
" color:#030202;\n"
" padding-top:5px;\n"
" padding-bottom:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(181, 121, 0);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.hboxlayout.addWidget(self.pushButton_5)
        self.verticalLayout_2.addLayout(self.hboxlayout)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem12)
        self.gridLayout.addWidget(self.frame_6, 3, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem13, 1, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem14, 2, 1, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem15, 1, 2, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet("background:none;\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 0, 0);\n"
"border-radius:30px;\n"
"border:2px solid #030202;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setStyleSheet("background-color: rgb(204, 204, 204);\n"
" border:2px solid #030202;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.frame_7)
        self.listWidget.setMinimumSize(QtCore.QSize(250, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.listWidget.setFont(font)
        self.listWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setStyleSheet(" border:None\n"
"")
        self.listWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget.setTabKeyNavigation(False)
        self.listWidget.setMovement(QtWidgets.QListView.Free)
        self.listWidget.setResizeMode(QtWidgets.QListView.Fixed)
        self.listWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget.setUniformItemSizes(True)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.verticalLayout.addWidget(self.listWidget)
        self.gridLayout_7.addWidget(self.frame_7, 4, 3, 5, 3)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setStyleSheet("border:none;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/bg/images/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_7.addWidget(self.pushButton_3, 3, 5, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(" border:None;")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_7.addWidget(self.label_14, 3, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(" border:None;")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_7.addWidget(self.label_15, 7, 1, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet("background-color: rgb(204, 204, 204); border:2px solid #030202;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_8.setContentsMargins(15, -1, -1, -1)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background: None; border:None;")
        self.label_7.setObjectName("label_7")
        self.gridLayout_8.addWidget(self.label_7, 8, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background: None; border:None;")
        self.label_5.setObjectName("label_5")
        self.gridLayout_8.addWidget(self.label_5, 2, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background: None; border:None;")
        self.label_6.setObjectName("label_6")
        self.gridLayout_8.addWidget(self.label_6, 3, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background: None; border:None;")
        self.label_10.setObjectName("label_10")
        self.gridLayout_8.addWidget(self.label_10, 7, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background: None; border:None;")
        self.label_12.setObjectName("label_12")
        self.gridLayout_8.addWidget(self.label_12, 5, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background: None; border:None;")
        self.label_8.setObjectName("label_8")
        self.gridLayout_8.addWidget(self.label_8, 6, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background: None; border:None;")
        self.label_11.setObjectName("label_11")
        self.gridLayout_8.addWidget(self.label_11, 4, 2, 1, 1)
        self.gridLayout_7.addWidget(self.frame_3, 8, 1, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setAutoFillBackground(False)
        self.frame_5.setStyleSheet("background-color: rgb(204, 204, 204);\n"
"border:2px solid #030202;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_10.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.frame_5)
        self.webEngineView.setMinimumSize(QtCore.QSize(725, 300))
        self.webEngineView.setMaximumSize(QtCore.QSize(725, 400))
        self.webEngineView.setStyleSheet("border:None;\n"
"border-radius:6px;\n"
"padding-top:5px;\n"
"padding-bottom:5px;")
        self.webEngineView.setProperty("url", QtCore.QUrl("https://www.google.com"))
        self.webEngineView.setObjectName("webEngineView")
        self.gridLayout_10.addWidget(self.webEngineView, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frame_5, 5, 0, 2, 2)
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(" border:None;")
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_7.addWidget(self.label_13, 3, 4, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_9.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton{background:none;\n"
" border:2px solid #030202;\n"
" border-radius:6px;\n"
" color:#030202;\n"
" padding-top:5px;\n"
" padding-bottom:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_7.addWidget(self.pushButton_9, 9, 1, 1, 1)
        self.gridLayout_6.addWidget(self.frame_2, 1, 1, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem16, 0, 1, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.gridLayout_5.addWidget(self.stackedWidget, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1095, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.listWidget.setCurrentRow(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Restaurant Predictor"))
        self.label_3.setText(_translate("MainWindow", "Password:"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "abc@xyz.com"))
        self.pushButton_2.setText(_translate("MainWindow", "Signup"))
        self.pushButton.setText(_translate("MainWindow", "login"))
        self.label_2.setText(_translate("MainWindow", "Email:"))
        self.pushButton_6.setText(_translate("MainWindow", "Predict Restaurant "))
        self.pushButton_7.setText(_translate("MainWindow", "About"))
        self.pushButton_8.setText(_translate("MainWindow", "Favourite"))
        self.pushButton_10.setText(_translate("MainWindow", "Logout"))
        self.label_9.setText(_translate("MainWindow", "Select Features"))
        self.label_4.setText(_translate("MainWindow", "Select City"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Birmingham"))
        self.comboBox.setItemText(1, _translate("MainWindow", "London"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Manchester"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Edinburgh"))
        self.comboBox.setItemText(4, _translate("MainWindow", "New Delhi"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Mumbai"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Dubai"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Athens"))
        self.pushButton_4.setText(_translate("MainWindow", "Next"))
        self.pushButton_5.setText(_translate("MainWindow", "Back"))
        self.listWidget.setSortingEnabled(True)
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Resta"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Restaurant 1"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_14.setText(_translate("MainWindow", "Location on map"))
        self.label_15.setText(_translate("MainWindow", "Restaurant Details"))
        self.label_7.setText(_translate("MainWindow", "Address"))
        self.label_5.setText(_translate("MainWindow", "Restaurant name"))
        self.label_6.setText(_translate("MainWindow", "Restaurant_ID"))
        self.label_10.setText(_translate("MainWindow", "locality"))
        self.label_12.setText(_translate("MainWindow", "Currency"))
        self.label_8.setText(_translate("MainWindow", "City"))
        self.label_11.setText(_translate("MainWindow", "Cuisines"))
        self.label_13.setText(_translate("MainWindow", "Select Restaurant"))
        self.pushButton_9.setText(_translate("MainWindow", "Add to Favourite"))
from PyQt5 import QtWebEngineWidgets
import images


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
