from sys import argv as av
from src.train_model import train_model
from src.test_model import test_model

def help():
    print ("USAGE")
    print("\tpython3 submission.py --train <path_to_train_dataset.csv> --test <path_to_test_dataset.csv>")
    print("DESCRIPTION")
    print("\tRun to train model on custom dataset or to re-train the model on default datasets")
    print("\tIf no argument is provided, the program will run with the defaults .csv in the /datasets folder")

def get_paths():

    paths = ['datasets/train.csv', 'datasets/test_x.csv']

    if (len(av) > 1):
        if (av[1] == "--help" or av[1] == "-h"):
            help()
            exit(0)
        for i in range(0,len(av)):
            print (i)
            if (av[i] == "--train"):
                paths[0] = av[i + 1]
            if (av[i] == "--test"):
                paths[1] = av[i + 1]
    return paths


def main():

    paths = get_paths()

    model = train_model(paths[0])
    test_model(model, paths[1])
    exit (0)


if __name__ == '__main__':
    main()