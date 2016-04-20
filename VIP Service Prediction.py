# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 18:23:13 2016

@author: YI
"""

import json
import csv
import pandas as pd



#read json
data = []
with open('user.json') as f:
    for line in f:
        data.append(json.loads(line))

#convert json to csv
filecsv = csv.writer(open('user.csv','w'))
count = 0
for line in data:
    if count == 0:
        header = line.keys()
        filecsv.writerow(header)
        count += 1
    filecsv.writerow((line.values())


#read csv
df= pd.read_csv('user.csv')
