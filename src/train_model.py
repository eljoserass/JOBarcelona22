import pandas as pd
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.metrics import f1_score


def train_model (path):

    # get training dataset
    training_data = pd.read_csv(path, index_col=0, parse_dates=True)

    # clean time data
    training_data['Minutes'] = (training_data['Hour']*60) + training_data['Minutes']
    del training_data['Hour']

    # get attribute vector
    x = training_data.iloc[:,0:7]

    # initialize knn object and train model
    knn = KNN(n_neighbors=3)
    knn.fit(x, training_data['Insect'])

    # add predicted target to attribute vector
    x['Insect'] = knn.predict(x)

    # print score comparing targets
    print ('f1_score:', f1_score(training_data['Insect'], x['Insect'], average='macro'))
    return (knn)