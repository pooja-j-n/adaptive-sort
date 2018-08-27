#include "stdafx.h"

#include <iostream>
#include <stdlib.h>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

class MergeSort {

public:

	MergeSort();

	void SortFunc(vector<unsigned long int>& vec, int l, int m, int r);

	void Sort(vector<unsigned long int>& vec, int l, int r);


};