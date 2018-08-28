
//#include <iostream>
//#include <stdlib.h>
//#include <time.h>
//#include <chrono>
//#include <vector>
//#include <fstream>
//#include <string>
//#include <iterator>

#include "sortingParameters.h"
#include "MergeSort.h"
#include "InsertionSort.h"
#include "QuickSort.h"


using namespace std;

class SortCaller {

	vector<unsigned long int> inputVector;
	sortingParameters inputParam;

public:

	SortCaller();

	SortCaller(vector<unsigned long int> vec, sortingParameters param);

	void CallSortOnVector();
};