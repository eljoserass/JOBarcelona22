##
## DATA-SCIENCE PROJECT, 2021
## JOBarcelona22
## File description: train_model and test_model methods
## Submission.py
##

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.metrics import f1_score
from sys import argv as av

OPTIMUM_N_NEIGHBORS = 3

class Submission:

    def __init__(self):
        self.__test_path = 'datasets/test_x.csv'
        self.__train_path = 'datasets/train.csv'
        self.__model = KNN(n_neighbors=OPTIMUM_N_NEIGHBORS)

    def __train_model(self):

        """
            Solution for classification problem.
            This function train a K-Nearest Neighbors
        """

        """ get training dataset """
        training_data = pd.read_csv(self.__train_path, index_col=0, parse_dates=True)

        """ clean time data """
        training_data['Minutes'] = training_data['Hour'] * 60 + training_data['Minutes']
        del training_data['Hour']

        """ get attribute vector """
        x = training_data.iloc[:,0:7]

        """ initialize knn object and fit data into the model """
        self.__model.fit(x, training_data['Insect'])

        """ predict target to test score with previously seen data """
        y = self.__model.predict(x)

        print ('f1_score:', f1_score(training_data['Insect'], y, average='macro'))

    def __test_model(self):

        """
            Function to use the trained model for making predictions with unseen data
            Write results in results.csv in this format:
            Test_index,Insect
            7000,1
            7001,0
        """

        """ get testing dataset """
        test_data = pd.read_csv(self.__test_path, index_col=0, parse_dates=True)

        """ clean time data """
        test_data['Minutes'] = (test_data['Hour']*60) + test_data['Minutes']
        del test_data['Hour']

        """ get prediciton target """
        y = self.__model.predict(test_data)

        """ write results """
        result = pd.DataFrame({'Test_index': list(test_data.index.values), 'Insect': y})
        result.to_csv('results.csv', index=False)

    def ___store_paths(self):

        """
            Function for getting the path files passed as arguments
        """

        if (len(av) > 1):
            if (av[1] == "--help" or av[1] == "-h"):
                self.helper()
                exit (0)
            for i in range(0,len(av)):
                if (av[i] == "--train"):
                    self.__train_path = av[i + 1]
                if (av[i] == "--test"):
                    self.__test_path = av[i + 1]

    def helper(self):
        print ("USAGE")
        print ("\t./program --train <path_to_train_dataset.csv> --test <path_to_test_dataset.csv>")
        print ("DESCRIPTION")
        print ("\tUse --train and --test to train and test model on custom dataset")
        print ("\tIf no argument is provided, the program will run with the defaults .csv in the /datasets folder")
        print ("\tThe results will be written in a .csv file called results.csv")


    def run(self):
        self.___store_paths()
        self.__train_model()
        self.__test_model()