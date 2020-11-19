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
from MainWindow3 import Ui_MainWindow
from googletrans import Translator, LANGUAGES
#import itertools
import re

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.xlsxFile = os.path.join(os.getcwd(), 'Werkwoorden_Lijst.xlsx')
        self.chosenTable = ''
        self.translator = Translator()
        self.defaultLangs = ['en', 'nl']

        # self.initialiseMenuBar()
        self.initialiseWidgets()
        self.initialiseTable()

        logging.debug("Initialisation is done")

    # def initialiseMenuBar(self):
    #     # Create new action
    #     openAction = QtWidgets.QAction('&Open', self)        
    #     openAction.setShortcut('Ctrl+O')
    #     openAction.setStatusTip('Open document')
    #     openAction.triggered.connect(self.fileMenuOpenAction)
    #     # Menu bar
    #     menuBar = self.menuBar()
    #     fileMenu = menuBar.addMenu('&File')
    #     fileMenu.addAction(openAction)
    #     logging.debug("Initialise meub bar done")
    
    def initialiseWidgets(self):
        self.labelSearchResult.setHidden(True)
        self.textEditSearch.setAlignment(QtCore.Qt.AlignBottom)
        self.isShownMainTable = True
        self.buttonCheck.clicked.connect(self.buttonCheck_on_click)
        self.buttonMemory.clicked.connect(self.buttonMemory_on_click)
        self.buttonBack.clicked.connect(self.buttonBack_on_click)
        self.buttonSave.clicked.connect(self.buttonSave_on_click)
        self.buttonQuit1.clicked.connect(self.buttonQuit_on_click)
        self.buttonQuit2.clicked.connect(self.buttonQuit_on_click)
        self.textEditSearch.textChanged.connect(self.search_as_you_type)
        self.buttonTranslate.clicked.connect(self.buttonTranslate_on_click)
        self.tableWidget.itemChanged.connect(self.prepareForSaving)
        self.buttonCheck.setHidden(True)
        self.buttonSave.setHidden(True)
        self.buttonBack.setHidden(True)
        self.labelFrom.setHidden(True)
        self.labelTo.setHidden(True)
        self.comboBoxRangeStart.setHidden(True)
        self.comboBoxRangeEnd.setHidden(True)
        self.memoryMode = False
        self.resetMode = False
        self.searchMode = False
        self.langDict = dict((v.capitalize(),k) for k, v in LANGUAGES.items())
        self.comboBoxLang.addItems(self.langDict.keys())
        self.comboBoxLang.currentIndexChanged.connect(self.changeTranslationLang)
        self.comboBoxLang.setCurrentText('English')
        difficulties = [str(i+1) for i in range(4)]
        self.comboBoxDifficulty.addItems(difficulties)
        self.comboBoxRangeType.addItems(['Alphabet', 'Number'])
        self.comboBoxRangeType.currentIndexChanged.connect(self.changeRangeType)
        self.plainTextInput.installEventFilter(self)
        self.plainTextInput.hasSelected = False
        self.comboBoxRangeStart.currentIndexChanged.connect(self.changeStartWord)
        self.prepareForMemoryMode()

        
        # note area
        self.checkBox.toggled.connect(self.checkBox_on_stateChanged)
        self.checkBox_on_stateChanged()
        self.pushButtonNoteOpen.clicked.connect(self.buttonNoteOpen_on_click)
        self.pushButtonNoteSave.clicked.connect(self.buttonNoteSave_on_click)
        self.pushButtonNoteNew.clicked.connect(self.buttonNoteNew_on_click)
        self.notePath = ''

        openAction = QtWidgets.QAction('&Open', self)        
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open document')
        openAction.triggered.connect(self.fileMenuOpenAction)
        # self.checkBox.checkStateSet()
        logging.debug("intialise widgets done")
        
    def comboBoxTable_on_change(self):
        sheet_name = self.comboBoxTable.currentText()
        self.df = self.dfs[sheet_name]
        self.columnNames = list(self.df.columns)
        self.df = self.df.drop_duplicates(subset = [self.columnNames[1]])
        self.df = self.df.fillna('')
        self.df = self.df.sort_values(by=['Infinitief']).reset_index(drop=True)
        # self.df['Group'] = self.df['Group']
        self.df['Group'] = self.df['Infinitief'].apply(lambda x: x[0].upper())#Group by first letter
        self.numTableCol = len(self.columnNames)
        self.tableWidget.setColumnCount(self.numTableCol)     #Set number of columns
        self.tableWidget.setRowCount(len(self.df))        # and one row
 
        # Set the table
        self.tableWidget.setHorizontalHeaderLabels(self.columnNames)
        self.updateTable()
        self.updateCorpusDict()
    
    def checkBox_on_stateChanged(self):
        if self.checkBox.checkState() == 0:
            self.pushButtonNoteOpen.setHidden(True)
            self.pushButtonNoteSave.setHidden(True)
            self.pushButtonNoteNew.setHidden(True)
            self.buttonQuit1.setHidden(False)
            self.buttonQuit2.setHidden(True)
            self.textEditNote.setHidden(True)
        else:
            self.pushButtonNoteOpen.setHidden(False)
            self.pushButtonNoteSave.setHidden(False)
            self.pushButtonNoteNew.setHidden(False)
            self.buttonQuit1.setHidden(True)
            self.buttonQuit2.setHidden(False)
            self.textEditNote.setHidden(False)
    
    def buttonNoteNew_on_click(self):
        self.textEditNote.clear()
        self.notePath = ''
    
    def buttonNoteOpen_on_click(self):
        files_types = "Text Document (*.txt)"
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"Choose note file", "", files_types, options=options)
        if fileName:
            with open(fileName, 'rt') as f:
                self.notePath = fileName
                self.textEditNote.clear()
                for line in f.readlines():
                    line = line.replace('\n', '')
                    self.textEditNote.append(line)
                logging.debug("Openning note {}".format(fileName))   
        # cursor = self.textEditNote.textCursor()
        # selectedText = cursor.selectedText()
        # old_charfmt  = self.textEditNote.currentCharFormat()
        # cursor.movePosition(cursor.End)
        # new_charfmt  = old_charfmt
        # new_charfmt.setUnderlineColor(QtGui.QColor('Red'))
        # new_charfmt.setUnderlineStyle(QtGui.QTextCharFormat.WaveUnderline)
        # self.textEditNote.setCurrentCharFormat(new_charfmt)
        # self.textEditNote.append(selectedText)
        # self.textEditNote.setCurrentCharFormat(old_charfmt)
        # cursor.insertHtml("<span style=\"text-decoration: underline;\">"+selectedText+"</span>"); # make them ugly
        # cursor.insertHtml("<span style=\"color:blue;text-decoration:underline\"><span style=\"color:red\">"+selectedText+"</span></span>")
        # pass
        # cursor.insertHtml("<span style=\" text-decoration-color:red;text-decoration:underline\"><span style=\"text-decoration-style: wavy\">"+selectedText+"</span></span>")
    
    def buttonNoteSave_on_click(self):
        if len(self.notePath) == 0:
            files_types = "Text Document (*.txt)"
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
            fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self,"Save note file", "", files_types, options=options)
            if fileName:
                self.notePath = fileName
                logging.debug("Saving note {}".format(self.notePath))   
        else:   
            logging.debug("Appending note {}".format(self.notePath))
        if len(self.notePath) > 0:
            with open(self.notePath, 'wt') as f:
                f.write(self.textEditNote.toPlainText())
                logging.debug("Writting note {}".format(self.notePath))  
    
    
    def changeRangeType(self):
        items = self.getMemoryItems()
        self.comboBoxRangeStart.clear()
        self.comboBoxRangeStart.addItems(items)
        self.comboBoxRangeStart.adjustSize()
        self.comboBoxRangeEnd.clear()
        self.comboBoxRangeEnd.addItems(items)
        self.comboBoxRangeEnd.adjustSize()
        self.comboBoxRangeEnd.setCurrentText(items[-1])
    
    def getMemoryItems(self):
        if self.comboBoxRangeType.currentText() == 'Alphabet':
            items = sorted(list(set(list(self.df['Group']))))#sorted group
        else:
            items = [str(i+1) for i in range(len(self.df))]
        return items
    
    def changeStartWord(self):
        # items = sorted(list(set(list(self.df['Group']))))#sorted group
        items = self.getMemoryItems()
        starItem = self.comboBoxRangeStart.currentText()
        if starItem in items:
            startIdx = items.index(starItem)
            if not self.memoryMode:
                self.comboBoxRangeEnd.addItems(items[startIdx:])
                self.comboBoxRangeEnd.setCurrentText(items[-1])
            else:
                currentEndItem = self.comboBoxRangeEnd.currentText()
                self.comboBoxRangeEnd.clear()
                self.comboBoxRangeEnd.addItems(items[startIdx:])
                if currentEndItem in items:
                    currentEndIdx = items.index(currentEndItem)
                    if currentEndIdx < startIdx:
                        self.comboBoxRangeEnd.setCurrentText(items[-1])
                    else:
                        self.comboBoxRangeEnd.setCurrentText(currentEndItem)
                else:
                    self.comboBoxRangeEnd.setCurrentText(items[-1])
    
    def prepareForMemoryMode(self):
        if not self.memoryMode:
            self.buttonCheck.setHidden(True)
            self.buttonBack.setHidden(True)
            self.labelFrom.setHidden(True)
            self.labelTo.setHidden(True)
            self.comboBoxRangeStart.setHidden(True)
            self.comboBoxRangeEnd.setHidden(True)
            self.comboBoxRangeType.setHidden(True)
        else:
            self.buttonCheck.setHidden(False)
            self.buttonBack.setHidden(False)
            self.buttonSave.setHidden(True)
            self.labelFrom.setHidden(False)
            self.labelTo.setHidden(False)
            self.comboBoxRangeStart.setHidden(False)
            self.comboBoxRangeEnd.setHidden(False)
            self.comboBoxRangeType.setHidden(False)
    
    
    def fileMenuOpenAction(self):
        files_types = "CSV (*.csv);;Microsoft spreedsheets (*.xlsx);;Microsoft spreedsheets (*.xls)"
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QtWidgets.QFileDialog.getOpenFileName()", "", files_types, options=options)
        if fileName:
            self.xlsxFile = fileName
            self.initialiseTable()
            logging.debug("Openning file {}".format(fileName))
            
    
    def changeTranslationLang(self):
        langText = self.comboBoxLang.currentText()
        lang     = self.langDict[langText]
        if lang in self.defaultLangs:
            self.plainTextOutput2.setHidden(True)
        else:
            self.plainTextOutput2.setHidden(False)
        
    
    def prepareForSaving(self, item):
        if not self.resetMode and not self.searchMode:
            if self.buttonSave.isHidden and not self.memoryMode:
                self.buttonSave.setHidden(False)
#            row = item.row()
#            col = item.column()
#            text = self.tableWidget.item(row, col).text()
#            if row == len(self.df_backup):
#                self.df_backup.loc[len(self.df_backup), :] = ''
#            self.df_backup.iloc[row, col] = text
#            self.tableWidget.resizeColumnsToContents()
    
    def eventFilter(self, widget, event):
        if (event.type() == QtCore.QEvent.KeyPress and
            widget is self.plainTextInput):
            key = event.key()
            modifiers = event.modifiers()
            if (modifiers == QtCore.Qt.ControlModifier) and (key == QtCore.Qt.Key_Return):
                self.plainTextInput.appendPlainText('')
                return True
            if key == QtCore.Qt.Key_Return:
                self.buttonTranslate_on_click()
                return True
        return QtWidgets.QWidget.eventFilter(self, widget, event)
    
    def resetTable(self):
        self.resetMode = True
        self.updateTable()    
        self.resetMode = False
        logging.debug("reseting table done")
        
    def buttonTranslate_on_click(self):
        input_str = self.plainTextInput.toPlainText()
        chosen_lang = self.langDict[self.comboBoxLang.currentText()]
        langs = self.defaultLangs + [chosen_lang.lower()]
        langs = list(set(langs))#remove duplicated
        try:
            lang_input = self.translator.detect(input_str).lang.lower()
            logging.debug("Input lange is {}".format(lang_input))
            if lang_input in langs:
                langs.remove(lang_input)
                for i in range(len(langs)):
                    if i == 0:
                        translated = self.translator.translate(input_str, src=lang_input, dest=langs[i])
                        self.plainTextOutput1.setPlainText(translated.text)
                    elif not self.plainTextOutput2.isHidden():
                        translated = self.translator.translate(input_str, src=lang_input, dest=langs[i])
                        self.plainTextOutput2.setPlainText(translated.text)
        except:
            pass
        # else:
            # if lang_input in LANGUAGES:
                # chosen_lang = LANGUAGES[lang_input]
                # self.comboBoxLang.setCurrentText(chosen_lang.capitalize())
                # self.buttonTranslate_on_click()
            # else:
                # self.plainTextOutput1.setPlaceholderText("Unknown lang: {}".format(lang_input))
    
    def buttonBack_on_click(self):
        self.resetTable()
        self.memoryMode = False
        self.prepareForMemoryMode()
    
    def checkEquality(self, userStr, correctStr):
        userStrList     = sorted(re.findall(r"[\w']+", userStr.lower()))
        correctStrList  = sorted(re.findall(r"[\w']+", correctStr.lower()))
        return userStrList == correctStrList
    
    def buttonCheck_on_click(self):
        for r in range(self.tableWidget.rowCount()):
            for c in range(self.tableWidget.columnCount()):
                value_correct = self.df_gap_origin.iloc[r,c]
                if type(value_correct) == str and self.df_gap.iloc[r,c] != value_correct: #must be a gap
                    value_user = self.tableWidget.item(r, c).text()
                    if self.checkEquality(value_user, value_correct):# correct answer mark as green
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
        string = self.textEditSearch.text()
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
        
    def getCurrentTable(self):
        numRow = self.tableWidget.rowCount()-1
        numCol = self.tableWidget.columnCount()
        self.df_backup = pd.DataFrame(np.zeros([numRow, numCol], dtype=float), columns=self.columnNames)
        for r in range(numRow):
            for c in range(numCol):
                self.df_backup.iloc[r,c] = self.tableWidget.item(r,c).text()
    
    def saveTable(self):
        book = load_workbook(self.xlsxFile)
        writer = pd.ExcelWriter(self.xlsxFile, engine='openpyxl')
        writer.book = book
        writer.sheets = {ws.title: ws for ws in book.worksheets}
        self.df_backup.to_excel(writer, sheet_name='Sheet1', startrow=1, header=False,index=False)
        writer.save()
        logging.debug("save table is done")
    
    def buttonMemory_on_click(self):
        difficulty = int(self.comboBoxDifficulty.currentText())
        # items = sorted(list(set(list(self.df['Group']))))#sorted group
        items = self.getMemoryItems()
        if not self.memoryMode:
            # items = [str(i+1) for i in range(len(self.df))]
            self.comboBoxRangeStart.addItems(items)
        # 
        if self.comboBoxRangeType.currentText() == 'Alphabet':
            startIdx = self.df[self.df['Group']==self.comboBoxRangeStart.currentText()].head(1).index[0]
            endIdx = self.df[self.df['Group']==self.comboBoxRangeEnd.currentText()].tail(1).index[0]
        else:
            startIdx = int(items.index(self.comboBoxRangeStart.currentText()))
            endIdx   = int(items.index(self.comboBoxRangeEnd.currentText()))+1
        numSample = endIdx - startIdx
        numSample = min([numSample, 10])
        df_temp = self.df[startIdx:endIdx].copy()
        # print('Length: {}\n {}'.format(len(df_temp), df_temp))
        self.df_temp = df_temp.copy()
        df = df_temp.sample(numSample).copy().reset_index(drop=True)
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
        self.memoryMode = True
        self.prepareForMemoryMode()
        logging.debug("enter memory mode")
        
    
    def buttonSave_on_click(self):
        self.getCurrentTable()
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
        logging.debug('Trying to read {}'.format(self.xlsxFile))
        self.dfs = pd.read_excel(self.xlsxFile, sheet_name=None)
        sheet_names = [sheet_name for sheet_name in self.dfs.keys() if len(re.findall('[0-9]', sheet_name)) == 0]
        self.comboBoxTable.addItems(sheet_names)
        self.comboBoxTable.setCurrentText(sheet_names[0])
        self.comboBoxTable.currentIndexChanged.connect(self.comboBoxTable_on_change)
        logging.debug('Read {} done'.format(self.xlsxFile))
        self.comboBoxTable_on_change()

        
        # Set the list
        self.comboBox.clear()
        self.comboBox.addItems(['Randomly']+self.columnNames)
#        self.tableWidths = [self.tableWidget.columnWidth(i) for i in range()
#        self.tableWidget.Box.
        logging.debug("intialise table done")
        
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
    os.environ['QT_IM_MODULE'] = 'fcitx'
    app = QtCore.QCoreApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())