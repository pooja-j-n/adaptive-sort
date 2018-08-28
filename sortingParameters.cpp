#include "stdafx.h"

#include "sortingParameters.h"



sortingParameters::sortingParameters()
{
}


sortingParameters::~sortingParameters()
{
}


void sortingParameters::display()
{
	cout << endl << "Sorting Parameters : " << endl;
	cout << "Size : " << size << endl;
	cout << "Range : " << range << endl;

	cout << "Sort Percentage : ";
	if (sortPercentage != 100)
		cout << sortPercentage;
	else
		cout << "Entire Array except the last element";
	cout << endl;

	cout << "Data type : " << dataType << endl;
	cout << "Data structure type : " << dataStructType << endl;
}


string sortingParameters::toString()
{
	ostringstream oss;
	oss << size << "," << range << "," << sortPercentage << "," << dataType << "," << dataStructType;
	return oss.str();
}