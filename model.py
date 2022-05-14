import pandas as pd
import numpy as np
# import tensorflow as tf
import matplotlib.pyplot as plt

training_data = pd.read_csv('train.csv', index_col=0, parse_dates=True)

training_data['Minutes'] = (training_data['Hour']*60) + training_data['Minutes']
del training_data['Hour']

plt.scatter(training_data['Sensor_alpha'], training_data['Sensor_beta'])
plt.show()

print(training_data)