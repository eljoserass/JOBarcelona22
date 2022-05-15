import pickle
import pandas as pd

#insects_clusters_labels = {
#               2=1,
#               0=0,
#               2=1
#               }

test_data = pd.read_csv('test_x.csv', index_col=0, parse_dates=True)

loaded_model = pickle.load(open('model.sav', 'rb'))
# result = loaded_model.score(X_test, Y_test)
# print(result)

test_data['Minutes'] = (test_data['Hour']*60) + test_data['Minutes']
del test_data['Hour']