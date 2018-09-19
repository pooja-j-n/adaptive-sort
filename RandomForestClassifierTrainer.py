from sklearn.ensemble import RandomForestClassifier
from argparse import ArgumentParser
import numpy as np
import csv
import random
import pickle


DEFAULT_NUM_PARAMS = 3
DEFAULT_SPLIT_RATIO = 0.75
DEFAULT_DATASET_FILE = 'dataForDT.csv'
DEFAULT_CLASSIFIER_FILE = 'trainedClassifier.dat'


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument("-np", "--numParams", dest="num_params", type=int, default=DEFAULT_NUM_PARAMS,
                        help="The number of parameters."
                             "[Default : {0}]".format(DEFAULT_NUM_PARAMS))
    parser.add_argument("-sr", "--splitRatio", dest="split_ratio", type=float, default=DEFAULT_SPLIT_RATIO,
                        help="The dataset split ratio."
                             "[Default : {0}, Range : 0-1]".format(DEFAULT_SPLIT_RATIO))
    parser.add_argument("-df", "--datasetFile", dest="dataset_csv_file",
                        type=str, default=DEFAULT_DATASET_FILE,
                        help="The csv file containing sorting algorithm performance dataset."
                             "[Default : {0}]".format(DEFAULT_DATASET_FILE))
    parser.add_argument("-cf", "--classifierFile", dest="trained_classifier_file",
                        type=str, default=DEFAULT_CLASSIFIER_FILE,
                        help="The filename for storing the trained classifier."
                             "[Default : {0}]".format(DEFAULT_CLASSIFIER_FILE))
    args = parser.parse_args()
    if args.split_ratio > 1 or args.split_ratio < 0:
        parser.error("Invalid split ratio entered.")
    return args


def load_csv(filename):
    lines = csv.reader(open(filename, "rt"))
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [int(x) for x in dataset[i]]
    return dataset


def split_dataset(dataset, split_ratio):
    train_size = int(len(dataset) * split_ratio)
    train_set = []
    test_set = list(dataset)
    while len(train_set) < train_size:
        index = random.randrange(len(test_set))
        train_set.append(test_set.pop(index))
    print("\nDataset split ratio : {0}.".format(split_ratio))
    print("Training set : {0} rows".format(len(train_set)))
    print("Test set : {0} rows".format(len(test_set)))
    return [train_set, test_set]


def split_into_x_y(dataset, num_params):
    dataset_x = np.array(dataset)[:, :num_params]
    dataset_y = np.array(dataset)[:, -1]
    # TODO: remove this
    for i in range(len(dataset_y)):
        if dataset_y[i] != 1:
            dataset_y[i] = 2
    return dataset_x, dataset_y


def train_classifier(training_set, num_params):
    training_set_x, training_set_y = split_into_x_y(training_set, num_params)
    clf = RandomForestClassifier()
    clf.fit(training_set_x, training_set_y)
    print("\nClassifier trained successfully.")
    return clf


def calc_accuracy(clf, test_set, num_params):
    test_set_x, test_set_y = split_into_x_y(test_set, num_params)
    predicted = clf.predict(test_set_x)
    accuracy = np.count_nonzero(predicted == test_set_y) / len(test_set) * 100
    print("Accuracy : {0}%".format(accuracy))


def save_classifier(clf, trained_classifier_file):
    pickle_file = open(trained_classifier_file, 'wb')
    pickle.dump(clf, pickle_file)
    pickle_file.close()
    print("\nTrained classifier stored in the file [{0}]".format(trained_classifier_file))


def main():
    args = parse_arguments()
    dataset = load_csv(args.dataset_csv_file)
    training_set, test_set = split_dataset(dataset, args.split_ratio)
    clf = train_classifier(training_set, args.num_params)
    calc_accuracy(clf, test_set, args.num_params)
    save_classifier(clf, args.trained_classifier_file)


main()
