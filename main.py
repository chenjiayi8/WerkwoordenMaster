#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 21:31:53 2020

@author: frank
"""
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt
import pandas as pd
import numpy as np
 
class MainWindow(QMainWindow):
    # Override class constructor
    def __init__(self):
        self.xlsxFile = os.path.join(os.getcwd(), 'Resources', 'Werkwoorden_Lijst.xlsx')
        self.df = pd.read_excel(self.xlsxFile)
        # You must call the super class method
        QMainWindow.__init__(self)
 
        self.setMinimumSize(QSize(600, 80))         # Set sizes 
        self.setWindowTitle("Werkwoorden Master")    # Set the window title
        central_widget = QWidget(self)              # Create a central widget
        self.setCentralWidget(central_widget)       # Install the central widget
 
        grid_layout = QGridLayout(self)         # Create QGridLayout
        central_widget.setLayout(grid_layout)   # Set this layout in central widget
 
        self.initialiseTable()       
 
        grid_layout.addWidget(self.table, 0, 0)   # Adding the table to the grid
 
    def initialiseTable(self):
        self.table = QTableWidget(self)  # Create a table
        columnNames = list(self.df.columns)
        self.numTableCol = len(columnNames)
        self.table.setColumnCount(self.numTableCol)     #Set number of columns
        self.table.setRowCount(len(self.df))        # and one row
 
        # Set the table headers
        self.table.setHorizontalHeaderLabels(columnNames)
        self.updateTable()
        self.table.resizeColumnsToContents()
        
    def updateTable(self):
        for c in range(self.numTableCol):
#            self.table.horizontalHeaderItem(c).setTextAlignment(Qt.AlignHCenter)
            for r in range(len(self.df)):
                item = self.df.iloc[r,c]
                print(type(item))
                if type(item) == float:
                    if np.isnan(item):
                        item = ''
                    else:
                        item = str(item)
                self.table.setItem(r, c, QTableWidgetItem(item))
                
 
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())