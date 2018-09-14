from sklearn.ensemble import RandomForestClassifier
from argparse import ArgumentParser
import pickle

DEFAULT_LENGTH = 10000
DEFAULT_RANGE = 30000
DEFAULT_SORT_PERCENTAGE = 0
DEFAULT_CLASSIFIER_FILE = 'trainedClassifier.dat'


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument("params", nargs='*',
                        help="The parameters of the input data to be sorted in the order: "
                             "length, range, sort_percentage"
                        )
    parser.add_argument("-l", "--length", dest="length", type=int, default=DEFAULT_LENGTH,
                        help="The number of elements to be sorted."
                             "[Default : {0}]".format(DEFAULT_LENGTH))
    parser.add_argument("-r", "--range", dest="range", type=int, default=DEFAULT_RANGE,
                        help="Difference between maximum and minimum values of the data."
                             "[Default : {0}]".format(DEFAULT_RANGE))
    parser.add_argument("-s", "--sortPercentage", dest="sort_percentage", type=float, default=DEFAULT_SORT_PERCENTAGE,
                        help="The pre-sort percentage of the data."
                             "[Default : {0}, Range : 0-100]".format(DEFAULT_SORT_PERCENTAGE))
    parser.add_argument("-cf", "--classifierFile", dest="trained_classifier_file",
                        type=str, default=DEFAULT_CLASSIFIER_FILE,
                        help="The pickled file of trained classifier."
                             "[Default : {0}]".format(DEFAULT_CLASSIFIER_FILE))
    args = parser.parse_args()
    if args.sort_percentage > 100 or args.sort_percentage < 0:
        parser.error("Invalid sort percentage entered.")
    if not args.params:
        args.params = [args.length, args.range, args.sort_percentage]
    return args


def load_classifier(trained_classifier_file):
    pickle_file = open(trained_classifier_file, 'rb')
    clf = pickle.load(pickle_file)
    pickle_file.close()
    return clf


def main():
    args = parse_arguments()
    clf = load_classifier(args.trained_classifier_file)
    print(clf.predict([args.params])[0])


main()
