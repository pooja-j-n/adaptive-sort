from argparse import ArgumentParser
from tqdm import tqdm
import numpy as np
import csv
import random
import importlib
import operator
import sys

# TODO : remove this import
# currently added here to avoid printing of warning during dynamic import
from sklearn.ensemble import RandomForestClassifier


DEFAULT_NUM_ITERATIONS = 10
DEFAULT_NUM_PARAMS = 3
DEFAULT_SPLIT_RATIO = 0.75
DEFAULT_DATASET_FILE = 'dataForDT.csv'
DEFAULT_CLASSIFIER_LIST = [
    "KNeighborsClassifier",
    "DecisionTreeClassifier",
    "RandomForestClassifier",
    "MLPClassifier",
    "AdaBoostClassifier",
    "GaussianNB",
    "QuadraticDiscriminantAnalysis",
    "GradientBoostingClassifier",
]


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument("classifier_list", nargs='*', type=str, default=DEFAULT_CLASSIFIER_LIST,
                        help="The list of classifiers to be compared.\n"
                             "[Default : {0}]".format(DEFAULT_CLASSIFIER_LIST)
                        )
    parser.add_argument("-n", "--numIterations", dest="num_iterations", type=int, default=DEFAULT_NUM_ITERATIONS,
                        help="The number of times each classifier will be trained."
                             "[Default : {0}]".format(DEFAULT_NUM_ITERATIONS))
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
    return [train_set, test_set]


def split_into_x_y(dataset, num_params):
    dataset_x = np.array(dataset)[:, :num_params]
    dataset_y = np.array(dataset)[:, -1]
    # TODO: remove this
    for i in range(len(dataset_y)):
        if dataset_y[i] != 1:
            dataset_y[i] = 2
    return dataset_x, dataset_y


def get_classifier(classifier_name):
    module_list = ['ensemble', 'tree', 'naive_bayes', 'gaussian_process', 'gaussian_process.kernels', 'neural_network',
                   'svm', 'neighbors', 'discriminant_analysis', 'linear_model']
    for module_name in module_list:
        module = importlib.import_module('sklearn.' + module_name)
        classifier = getattr(module, classifier_name, None)
        if classifier is not None:
            return classifier()
    print("\nUnable to load the classifier [{0}]. Please provide a correct classifier name.".format(classifier_name))
    import sys
    sys.exit(1)


def train_classifier(clf_name, training_set, num_params):
    training_set_x, training_set_y = split_into_x_y(training_set, num_params)
    clf = get_classifier(clf_name)
    clf.fit(training_set_x, training_set_y)
    return clf


def calc_accuracy(clf, test_set, num_params):
    test_set_x, test_set_y = split_into_x_y(test_set, num_params)
    predicted = clf.predict(test_set_x)
    accuracy = np.count_nonzero(predicted == test_set_y) / len(test_set) * 100
    return accuracy


def main():
    args = parse_arguments()
    dataset = load_csv(args.dataset_csv_file)
    sys.stderr.flush()
    print("\nDataset split ratio : {0}.\n".format(args.split_ratio))
    accuracy_sum = {}
    for clf_name in args.classifier_list:
        accuracy_sum[clf_name] = 0.0
    sys.stdout.flush()
    progress_bar = tqdm(range(args.num_iterations * len(args.classifier_list)))
    for i in range(args.num_iterations):
        for clf_name in args.classifier_list:
            training_set, test_set = split_dataset(dataset, args.split_ratio)
            progress_bar.set_description("[ Itr {:5d} ] {:30s} ".format(i + 1, clf_name))
            clf = train_classifier(clf_name, training_set, args.num_params)
            accuracy_sum[clf_name] += calc_accuracy(clf, test_set, args.num_params)
            progress_bar.update(1)
    progress_bar.close()
    accuracy_sum_list = sorted(accuracy_sum.items(), key=operator.itemgetter(1))
    print("\n\nAverage accuracy : \n")
    for average_accuracy_element in accuracy_sum_list:
        print("{:30s} : {:f}%".format(average_accuracy_element[0], average_accuracy_element[1] / args.num_iterations))


main()
