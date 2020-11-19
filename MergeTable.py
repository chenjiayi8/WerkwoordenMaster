#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 19:33:48 2020

@author: frank
"""

import re

xlsxFile = os.path.join(os.getcwd(), 'Werkwoorden_Lijst.xlsx')
dfs = pd.read_excel(xlsxFile, sheet_name=None)
keys = list(dfs.keys())
keys.remove('Sheet1')

unique_keys = [ ''.join(re.findall('[a-zA-Z]', key)) for key in keys]
unique_keys = list(set(unique_keys))

book = load_workbook(xlsxFile)
writer = pd.ExcelWriter(xlsxFile, engine='openpyxl')
writer.book = book
writer.sheets = {ws.title: ws for ws in book.worksheets}

for unique_key in unique_keys:
    key_targets = [target for target in keys if unique_key in target]
    df_targets = [dfs[key] for key in key_targets]
    df = pd.concat(df_targets)
    df = df.drop_duplicates(subset=['infinitief'])
    df = df.sort_values(['infinitief'])
    df.to_excel(writer, sheet_name= unique_key, header=True,index=False)
    
writer.save()


    
