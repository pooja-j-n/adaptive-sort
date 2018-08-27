#include "stdafx.h"

#include <iostream>
#include <stdlib.h>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

class QuickSort {

public:

	QuickSort();

	void swap(unsigned long int* a, unsigned long int* b);

	int partition(vector<unsigned long int>& vec, int l, int r);

	void Sort(vector<unsigned long int>& vec, int l, int r);


};