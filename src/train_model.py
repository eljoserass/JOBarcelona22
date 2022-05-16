import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier as KNN
import pickle
from sklearn.metrics import f1_score, roc_auc_score, accuracy_score, precision_score, recall_score, precision_recall_curve
from sklearn.preprocessing import MinMaxScaler


training_data = pd.read_csv('datasets/train.csv', index_col=0, parse_dates=True)


# standarize time data
training_data['Minutes'] = (training_data['Hour']*60) + training_data['Minutes']
del training_data['Hour']

x = training_data.iloc[:,0:7]
# print (x)
# insects = training_data['Insect']
# del training_data['Insect']
# scaler = MinMaxScaler()
# x = scaler.fit_transform(x)
# print (x)
# training_data = scaler.fit_transform(training_data)
# training_data['Insect'] = insects


knn = KNN(n_neighbors=3)
knn.fit(x, training_data['Insect'])

x['Insect'] = knn.predict(x)

print (f1_score(training_data['Insect'], x['Insect'], average='macro'))

# x['Insect'] = knn.predict(x)

def is_equal(val1, val2):
    return val1 == val2

def hit_miss_uwu(frame1, frame2):
    arr = []
    hit = 0
    miss = 0
    for i in range(0,len(frame1)):
        arr.append(is_equal(frame1['Insect'][i], frame2['Insect'][i]))
    for i in range(0,len(arr)):
        if arr[i]:
            hit +=1
        else:
            miss +=1

    print ("Hits: ",hit)
    print ("Miss: ", miss)
    print ((hit * 100) / len(frame1), "% accuracy")

# hit_miss_uwu(x, training_data)


# result = pd.DataFrame({'index' : x[0], 'prediction':x['Insect']})

