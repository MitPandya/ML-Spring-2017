import csv
import MDP_process2
from pandas import read_csv
import pandas as pd
import numpy as np

included_cols = [0, 1, 2, 3, 4, 5]
#, 25, 119, 120, 57, 74, 123, 12, 106, 30]


with open('MDP_Original_data2.csv', 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    with open('SFS.csv', 'w') as newcsv:
        writer = csv.writer(newcsv, delimiter = ',')
        for row in reader:
            colmn = list(row[i] for i in included_cols)
            zip(*colmn)
            writer.writerow(colmn)
    newcsv.close()
csv_file.close()

selected_colms = [25, 119, 120, 57, 74, 123, 12, 106, 30]

filepath = "MDP_Original_data2.csv"
dataframe = read_csv(filepath)
array = dataframe.values
for i in selected_colms:
    X = array[1:,i]
    Xfinal = X.astype(np.float)
    min_value = min(Xfinal)
    max_value = max(Xfinal)
    #print(min_value, max_value)
    a = sorted(Xfinal)
    #b = map(lambda x:x+1, a)
    l = len(a)
    b1 = a[int(l/4)]
    b2 = a[int(l/2)]
    b3 = a[int(3*l/4)]
    '''if (b1 == 0):
        b1 = a[int(l/3)]
        if (b1 == 0):
            b1 = a[int(l/2)]
    print(b1)

    if (b1 != 0):
        factor = pd.cut(Xfinal, [min_value,min_value+b1,min_value+2*b1,min_value+3*b1,max_value])
    else:
        factor = pd.cut(Xfinal, [-np.inf, b1+0.001, np.inf])'''
    pandalist = [-np.inf, b1, b2, b3, max_value]
    pandalist = sorted(list(set(pandalist)))
    label = []
    for i in range(len(pandalist)-1):
        label.append(i)
    #print(min_value, b1, b2, b3, max_value)
    #print(pandalist)
    factor = pd.cut(Xfinal, pandalist, labels = label)
    #print(factor)
    #print(pd.value_counts(factor))
    arr = factor[0:,]
    #print(arr[1])
    with open('SFS_values.csv', 'w') as SFS:
        writer = csv.writer(newcsv, delimiter = ',')
        for i in range(7168):
            #print(i)
            #i = list(i)
            #zip(arr[i])
            writer.writerow(arr[i])
    SFS.close()
    #print(np.histogram(a))

#MDP_process2.induce_policy_MDP('SFS.csv')
