# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 18:23:13 2016

@author: YI
"""

import json
import csv
import numpy as np
import pandas as pd

b= pd.read_csv('user.csv')

#read json
data = []
with open('user.json') as f:
    for line in f:
        data.append(json.loads(line))

a = csv.writer(open('user1.csv','w'))
a.writerow['appfile','uid','app','label','activity_time','category_id']
                   


filecsv = csv.writer(open('user.csv','w'))
count = 0
for line in data:
    if count == 0:
        header = line.keys()
        filecsv.writerow(header)
        count += 1
    filecsv.writerow((line.values())


a = np.loadtxt('user.csv')

'''
columns = map(lambda x: x.keys(), data)
columns = columns[0]
filecsv.writerow(columns)

for line in data:
    filecsv.writerow( map( lambda x: line.get( x, "" ), columns ) )


with open('user.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')

with open('eggs.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ')
'''