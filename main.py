#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 21:31:53 2020

@author: frank
"""
import os
from PyQt5 import QtWidgets, QtCore, QtGui
import pandas as pd
import numpy as np
import sys
from itertools import combinations 


from MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        self.xlsxFile = os.path.join(os.getcwd(), 'Resources', 'Werkwoorden_Lijst.xlsx')
        self.df = pd.read_excel(self.xlsxFile)
        self.df = self.df.drop_duplicates(subset = ["Infinitief"])
        self.labelSearchResult.setHidden(True)
        self.textEditSearch.setAlignment(QtCore.Qt.AlignBottom)
#        central_widget = QtWidgets.QWidget(self)              # Create a central widget
#        self.setCentralWidget(central_widget)       # Install the central widget
# 
#        grid_layout = QtWidgets.QGridLayout(self)         # Create QGridLayout
#        central_widget.setLayout(grid_layout)   # Set this layout in central widget
# 
        self.initialiseTable()
        self.buttonCheck.clicked.connect(self.buttonCheck_on_click)
        self.buttonMemory.clicked.connect(self.buttonMemory_on_click)
        self.buttonSave.clicked.connect(self.buttonSave_on_click)
        self.buttonQuit.clicked.connect(self.buttonQuit_on_click)
        self.textEditSearch.textChanged.connect(self.search_as_you_type)
#        grid_layout.addWidget(label1, 0, 0) 
#        grid_layout.addWidget(button1, 1, 0) 
#        grid_layout.addWidget(button2, 2, 0) 
#        grid_layout.addWidget(self.table, 2, 1)   # Adding the table to the grid
    
    def keyPressEvent(self, e):
        print(e.key())
#        self.buttonSearch_on_click()
        if e.key() == QtCore.Qt.Key_F5:
            self.close()
            
    def buttonCheck_on_click(self):
        self.tableWidget.item(2,2).setForeground(QtGui.QBrush(QtGui.QColor(0, 255, 0)))
        self.tableWidget.item(3,4).setForeground(QtGui.QBrush(QtGui.QColor(255, 0, 0)))
        print('button check click')
        
    def search_as_you_type(self):
        self.labelSearchResult.setHidden(True)
        string = self.textEditSearch.toPlainText()
        if len(string) > 0:
            if string in self.corpusDict:
                targetRows = self.corpusDict[string]
#                if len(targetRows) == 1:
#                    targetRows = targetRows[0]
                df = self.df.iloc[targetRows, :]
                self.updateTable(df)
            else:
                self.labelSearchResult.setHidden(False)
                self.labelSearchResult.setText("Nothing is found")
        else:
            self.updateTable()
        
    def buttonMemory_on_click(self):
        df = self.df.sample(10)
        self.updateTable(df)
        print('button memory click')
        
    def buttonSave_on_click(self):
        print('button save click')
        
    def buttonQuit_on_click(self):
        print('button quit click')
        self.close()
    
    def getCorpusList(self, string):
        string = string.lower()
        corpusList = [string[x:y] for x, y in combinations( 
            range(len(string) + 1), r = 2)] 
        return corpusList
    
    def updateCorpusDict(self):
        self.corpusDict = {}
        for c in range(self.numTableCol):
            for r in range(len(self.df)):
                item = self.df.iloc[r,c]
                if type(item) == str:
                    corpusList = self.getCorpusList(item)
                    for item in corpusList:
                        if item in self.corpusDict:
                            value = self.corpusDict[item]
                            value.append(r)
                            self.corpusDict[item] = list(set(value))
                        else:
                            self.corpusDict[item] = [r]
                    
    
    def initialiseTable(self):
        columnNames = list(self.df.columns)
        self.numTableCol = len(columnNames)
        self.tableWidget.setColumnCount(self.numTableCol)     #Set number of columns
        self.tableWidget.setRowCount(len(self.df))        # and one row
 
        # Set the table headers
        self.tableWidget.setHorizontalHeaderLabels(columnNames)
        self.updateTable()
        self.updateCorpusDict()
        
#        self.tableWidths = [self.tableWidget.columnWidth(i) for i in range()
#        self.tableWidget.Box.
        
    def emptyTable(self):
        for r in range(self.tableWidget.rowCount()):
            self.tableWidget.removeRow(r)
        self.tableWidget.setRowCount(0)
    
    def updateTable(self, df=[]):
        self.emptyTable()
        if len(df) == 0:
            df = self.df
        self.tableWidget.setRowCount(len(df))
        for c in range(self.numTableCol):
#            self.table.horizontalHeaderItem(c).setTextAlignment(Qt.AlignHCenter)
            for r in range(len(df)):
                item = df.iloc[r,c]
                if type(item) == float or type(item) == np.float64:
                    if np.isnan(item):
                        item = ''
                    else:
                        item = str(item)
                self.tableWidget.setItem(r, c, QtWidgets.QTableWidgetItem(item))
        self.tableWidget.resizeColumnsToContents()
#        self.tableWidget.horizontalHeader().setStretchLastSection(True)
                
 
if __name__ == "__main__":
    import sys
#    app = QtWidgets.QApplication(sys.argv)
    app = QtCore.QCoreApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())