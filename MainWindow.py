# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(842, 611)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 231, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelSearch = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelSearch.setObjectName("labelSearch")
        self.horizontalLayout.addWidget(self.labelSearch)
        self.textEditSearch = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.textEditSearch.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEditSearch.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEditSearch.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEditSearch.setObjectName("textEditSearch")
        self.horizontalLayout.addWidget(self.textEditSearch)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 70, 771, 461))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 530, 771, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buttonMemory = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.buttonMemory.setObjectName("buttonMemory")
        self.horizontalLayout_2.addWidget(self.buttonMemory)
        self.buttonCheck = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.buttonCheck.setObjectName("buttonCheck")
        self.horizontalLayout_2.addWidget(self.buttonCheck)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.buttonSave = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.buttonSave.setObjectName("buttonSave")
        self.horizontalLayout_2.addWidget(self.buttonSave)
        self.buttonQuit = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.buttonQuit.setObjectName("buttonQuit")
        self.horizontalLayout_2.addWidget(self.buttonQuit)
        self.labelSearchResult = QtWidgets.QLabel(self.centralwidget)
        self.labelSearchResult.setEnabled(True)
        self.labelSearchResult.setGeometry(QtCore.QRect(270, 20, 231, 39))
        self.labelSearchResult.setObjectName("labelSearchResult")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 842, 23))
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
        self.textEditSearch.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.buttonMemory.setText(_translate("MainWindow", "Memory"))
        self.buttonCheck.setText(_translate("MainWindow", "Check"))
        self.buttonSave.setText(_translate("MainWindow", "Save"))
        self.buttonQuit.setText(_translate("MainWindow", "Quit"))
        self.labelSearchResult.setText(_translate("MainWindow", "TextLabel"))

