
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier as KNN

def test_model(knn, path):

    # get testing dataset
    test_data = pd.read_csv(path, index_col=0, parse_dates=True)

    # clean time data
    test_data['Minutes'] = (test_data['Hour']*60) + test_data['Minutes']
    del test_data['Hour']

    # get prediciton target
    y = knn.predict(test_data)

    # write results
    result = pd.DataFrame({'Test_index': list(test_data.index.values), 'Insect': y})
    result.to_csv('results.csv')
