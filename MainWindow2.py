# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(857, 607)
        MainWindow.setMinimumSize(QtCore.QSize(0, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelSearch = QtWidgets.QLabel(self.centralwidget)
        self.labelSearch.setObjectName("labelSearch")
        self.horizontalLayout.addWidget(self.labelSearch)
        self.textEditSearch = QtWidgets.QLineEdit(self.centralwidget)
        self.textEditSearch.setObjectName("textEditSearch")
        self.horizontalLayout.addWidget(self.textEditSearch)
        self.labelSearchResult = QtWidgets.QLabel(self.centralwidget)
        self.labelSearchResult.setEnabled(True)
        self.labelSearchResult.setObjectName("labelSearchResult")
        self.horizontalLayout.addWidget(self.labelSearchResult)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 300))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.labelDifficulty = QtWidgets.QLabel(self.centralwidget)
        self.labelDifficulty.setObjectName("labelDifficulty")
        self.horizontalLayout_2.addWidget(self.labelDifficulty)
        self.comboBoxDifficulty = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxDifficulty.setObjectName("comboBoxDifficulty")
        self.horizontalLayout_2.addWidget(self.comboBoxDifficulty)
        self.buttonMemory = QtWidgets.QPushButton(self.centralwidget)
        self.buttonMemory.setObjectName("buttonMemory")
        self.horizontalLayout_2.addWidget(self.buttonMemory)
        self.buttonCheck = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCheck.setObjectName("buttonCheck")
        self.horizontalLayout_2.addWidget(self.buttonCheck)
        self.buttonBack = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBack.setObjectName("buttonBack")
        self.horizontalLayout_2.addWidget(self.buttonBack)
        self.labelFrom = QtWidgets.QLabel(self.centralwidget)
        self.labelFrom.setObjectName("labelFrom")
        self.horizontalLayout_2.addWidget(self.labelFrom)
        self.comboBoxRangeStart = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxRangeStart.setObjectName("comboBoxRangeStart")
        self.horizontalLayout_2.addWidget(self.comboBoxRangeStart)
        self.labelTo = QtWidgets.QLabel(self.centralwidget)
        self.labelTo.setObjectName("labelTo")
        self.horizontalLayout_2.addWidget(self.labelTo)
        self.comboBoxRangeEnd = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxRangeEnd.setObjectName("comboBoxRangeEnd")
        self.horizontalLayout_2.addWidget(self.comboBoxRangeEnd)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.buttonSave = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSave.setObjectName("buttonSave")
        self.horizontalLayout_2.addWidget(self.buttonSave)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.plainTextInput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextInput.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextInput.setFont(font)
        self.plainTextInput.setObjectName("plainTextInput")
        self.horizontalLayout_3.addWidget(self.plainTextInput, 0, QtCore.Qt.AlignBottom)
        self.plainTextOutput1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextOutput1.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextOutput1.setFont(font)
        self.plainTextOutput1.setReadOnly(True)
        self.plainTextOutput1.setObjectName("plainTextOutput1")
        self.horizontalLayout_3.addWidget(self.plainTextOutput1, 0, QtCore.Qt.AlignBottom)
        self.plainTextOutput2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextOutput2.setEnabled(True)
        self.plainTextOutput2.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextOutput2.setFont(font)
        self.plainTextOutput2.setReadOnly(True)
        self.plainTextOutput2.setObjectName("plainTextOutput2")
        self.horizontalLayout_3.addWidget(self.plainTextOutput2, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.buttonTranslate = QtWidgets.QPushButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Google_Translate_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonTranslate.setIcon(icon)
        self.buttonTranslate.setObjectName("buttonTranslate")
        self.horizontalLayout_4.addWidget(self.buttonTranslate)
        self.comboBoxLang = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxLang.setObjectName("comboBoxLang")
        self.horizontalLayout_4.addWidget(self.comboBoxLang)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.buttonQuit = QtWidgets.QPushButton(self.centralwidget)
        self.buttonQuit.setObjectName("buttonQuit")
        self.horizontalLayout_4.addWidget(self.buttonQuit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 857, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Werkwoorden Master"))
        self.labelSearch.setText(_translate("MainWindow", "Search:"))
        self.textEditSearch.setToolTip(_translate("MainWindow", "Search as you type"))
        self.labelSearchResult.setText(_translate("MainWindow", "TextLabel"))
        self.comboBox.setToolTip(_translate("MainWindow", "Memory randomly or choose a target column"))
        self.labelDifficulty.setText(_translate("MainWindow", "Difficulty"))
        self.buttonMemory.setToolTip(_translate("MainWindow", "Fill the gaps in the table"))
        self.buttonMemory.setText(_translate("MainWindow", "Memory"))
        self.buttonCheck.setToolTip(_translate("MainWindow", "Check the correct results"))
        self.buttonCheck.setText(_translate("MainWindow", "Check"))
        self.buttonBack.setToolTip(_translate("MainWindow", "Go back to main table"))
        self.buttonBack.setText(_translate("MainWindow", "Back"))
        self.labelFrom.setText(_translate("MainWindow", "From"))
        self.labelTo.setText(_translate("MainWindow", "To"))
        self.buttonSave.setToolTip(_translate("MainWindow", "Save the changes in main table"))
        self.buttonSave.setText(_translate("MainWindow", "Save"))
        self.plainTextInput.setToolTip(_translate("MainWindow", "Enter English, Dutch or another language to translate among these languages\n"
"(a)Enter to translate\n"
"(b)Ctrl+Enter to input multiply lines"))
        self.buttonTranslate.setToolTip(_translate("MainWindow", "Google translate"))
        self.buttonTranslate.setText(_translate("MainWindow", "Translate"))
        self.comboBoxLang.setToolTip(_translate("MainWindow", "Choose a third language other than English and Dutch"))
        self.buttonQuit.setToolTip(_translate("MainWindow", "Exit the app"))
        self.buttonQuit.setText(_translate("MainWindow", "Quit"))

