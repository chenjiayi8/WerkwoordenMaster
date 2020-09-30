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
from openpyxl import load_workbook
import logging
import random
from MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        self.xlsxFile = os.path.join(os.getcwd(), 'Werkwoorden_Lijst.xlsx')
        self.df = pd.read_excel(self.xlsxFile)
        self.df = self.df.drop_duplicates(subset = ["Infinitief"]).reset_index(drop=True)
        self.df = self.df.fillna('')
        self.df_backup = self.df.copy()
        self.labelSearchResult.setHidden(True)
        self.textEditSearch.setAlignment(QtCore.Qt.AlignBottom)
#        central_widget = QtWidgets.QWidget(self)              # Create a central widget
#        self.setCentralWidget(central_widget)       # Install the central widget
# 
#        grid_layout = QtWidgets.QGridLayout(self)         # Create QGridLayout
#        central_widget.setLayout(grid_layout)   # Set this layout in central widget
# 
        self.initialiseTable()
        self.isShownMainTable = True
        self.buttonCheck.clicked.connect(self.buttonCheck_on_click)
        self.buttonMemory.clicked.connect(self.buttonMemory_on_click)
        self.buttonBack.clicked.connect(self.buttonBack_on_click)
        self.buttonSave.clicked.connect(self.buttonSave_on_click)
        self.buttonQuit.clicked.connect(self.buttonQuit_on_click)
        self.textEditSearch.textChanged.connect(self.search_as_you_type)
#        self.tableWidget.cellChanged.connect(self.prepareForSaving)
        self.tableWidget.itemChanged.connect(self.prepareForSaving)
        self.buttonCheck.setHidden(True)
        self.buttonSave.setHidden(True)
        self.buttonBack.setHidden(True)
        self.memoryMode = False
        self.resetMode = False
        self.searchMode = False
        logging.debug("Initialisation is done")
#        grid_layout.addWidget(label1, 0, 0) 
#        grid_layout.addWidget(button1, 1, 0) 
#        grid_layout.addWidget(button2, 2, 0) 
#        grid_layout.addWidget(self.table, 2, 1)   # Adding the table to the grid
    
    def prepareForSaving(self, item):
        if not self.resetMode and not self.searchMode:
            if self.buttonSave.isHidden and not self.memoryMode:
                self.buttonSave.setHidden(False)
            row = item.row()
            col = item.column()
            text = self.tableWidget.item(row, col).text()
            if row == len(self.df_backup):
                self.df_backup.loc[len(self.df_backup), :] = ''
            self.df_backup.iloc[row, col] = text
            self.tableWidget.resizeColumnsToContents()
    
#    def keyPressEvent(self, e):
#        print(e.key())
#        if e.key() == QtCore.Qt.Key_F5:
#            self.close()
    
    def resetTable(self):
        self.resetMode = True
        self.updateTable()    
        self.resetMode = False
        logging.debug("reseting table done")
        
    
    def buttonBack_on_click(self):
        self.resetTable()
        self.memoryMode = False
        self.buttonCheck.setHidden(True)
        self.buttonBack.setHidden(True)
    
    def buttonCheck_on_click(self):
        for r in range(self.tableWidget.rowCount()):
            for c in range(self.tableWidget.columnCount()):
                value_correct = self.df_gap_origin.iloc[r,c]
                if type(value_correct) == str and self.df_gap.iloc[r,c] != value_correct: #must be a gap
                    value_user = self.tableWidget.item(r, c).text()
                    if value_user == value_correct:# correct answer mark as green
                        self.tableWidget.item(r,c).setForeground(QtGui.QBrush(QtGui.QColor(0, 255, 0)))
                    else:#fill correct value and mark as red
                        self.tableWidget.setItem(r, c, QtWidgets.QTableWidgetItem(value_correct))
                        self.tableWidget.item(r,c).setForeground(QtGui.QBrush(QtGui.QColor(255, 0, 0)))
                    self.tableWidget.item(r,c).setBackground(QtGui.QBrush(QtGui.QColor(230, 230, 230)))
        self.buttonCheck.setHidden(True)
        logging.debug("check results done")
        
    def search_as_you_type(self):
        logging.debug("start to search")
        self.labelSearchResult.setHidden(True)
        self.searchMode = True
        string = self.textEditSearch.toPlainText()
        if len(string) > 0:
            logging.debug("search word {}".format(string))
            if string in self.corpusDict:
                targetRows = self.corpusDict[string]
#                if len(targetRows) == 1:
#                    targetRows = targetRows[0]
                df = self.df.iloc[targetRows, :]
                self.updateTable(df)
                logging.debug("find word {}".format(string))
            else:
                self.labelSearchResult.setHidden(False)
                self.labelSearchResult.setText("Nothing is found")
                logging.debug("word {} is not found".format(string))
        else:
            self.resetTable()
        self.searchMode = False
        self.buttonSave.setHidden(True)
        self.buttonBack.setHidden(True)
        self.buttonCheck.setHidden(True)
        logging.debug("searching is done")
        
    def saveTable(self):
        book = load_workbook(self.xlsxFile)
        writer = pd.ExcelWriter(self.xlsxFile, engine='openpyxl')
        writer.book = book
        writer.sheets = {ws.title: ws for ws in book.worksheets}
        self.df_backup.to_excel(writer, sheet_name='Sheet1', startrow=1, header=False,index=False)
        writer.save()
        logging.debug("save table is done")
    
    def buttonMemory_on_click(self):
        difficulty = 1
        df = self.df.sample(10).copy().reset_index(drop=True)
        self.df_gap_origin = df.copy()
        df_gap = df.copy()
        memChoice = self.comboBox.currentText()
        for r in range(len(df_gap)):
            gap_columns= []
            gap_columns.extend(self.columnNames)
            if memChoice == 'Randomly':
                gap_column_idx = random.sample(range(len(gap_columns)), difficulty)
                gap_columns = [gap_columns[i] for i in gap_column_idx]
            else:
                gap_columns.remove(memChoice)
                gap_column_idx = random.sample(range(len(gap_columns)), difficulty-1)
                gap_columns = [gap_columns[i] for i in gap_column_idx]
                gap_columns.append(memChoice)
            for gap in gap_columns:
                df_gap.loc[r, gap] = ''
        self.updateTable(df_gap, gapMode=True)
        self.df_gap = df_gap
        self.buttonCheck.setHidden(False)
        self.buttonBack.setHidden(False)
        self.buttonSave.setHidden(True)
        self.memoryMode = True
        logging.debug("enter memory mode")
        
    
    def buttonSave_on_click(self):
        if self.df.equals(self.df_backup):
            logging.debug("Same tables, nothing to be saved")
        else:
            self.saveTable()
            logging.debug("New table is saved")
            self.df = self.df_backup.copy()
        
    def buttonQuit_on_click(self):
        logging.debug('button quit click')
        #popout dialog if df changed
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
        self.columnNames = list(self.df.columns)
        self.numTableCol = len(self.columnNames)
        self.tableWidget.setColumnCount(self.numTableCol)     #Set number of columns
        self.tableWidget.setRowCount(len(self.df))        # and one row
 
        # Set the table
        self.tableWidget.setHorizontalHeaderLabels(self.columnNames)
        self.updateTable()
        self.updateCorpusDict()
        
        # Set the list
        self.comboBox.addItems(['Randomly']+self.columnNames)
#        self.tableWidths = [self.tableWidget.columnWidth(i) for i in range()
#        self.tableWidget.Box.
        
    def emptyTable(self):
        for r in range(self.tableWidget.rowCount()):
            self.tableWidget.removeRow(r)
        self.tableWidget.setRowCount(0)
    
    def updateTable(self, df=[], gapMode=False):
        self.emptyTable()
        if len(df) == 0:
            df = self.df
            editMode = True
        else:
            editMode = False
        if editMode:
            self.tableWidget.setRowCount(len(df)+1)
        else:
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
                if gapMode:
                    if type(df.iloc[r,c]) == str and df.iloc[r,c] != self.df_gap_origin.iloc[r,c]:
                        self.tableWidget.item(r,c).setBackground(QtGui.QBrush(QtGui.QColor(230, 230, 230)))
            if editMode and  r == len(df) - 1:#add an empty row for adding new words
                self.tableWidget.setItem(r+1, c, QtWidgets.QTableWidgetItem(''))
        self.tableWidget.resizeColumnsToContents()
#        self.tableWidget.horizontalHeader().setStretchLastSection(True)
                
 
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, filename=os.path.join(os.getcwd(), 'log.txt'), format='%(asctime)s :: %(levelname)s :: %(message)s')
    import sys
#    app = QtWidgets.QApplication(sys.argv)
    app = QtCore.QCoreApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())