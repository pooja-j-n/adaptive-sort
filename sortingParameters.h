#pragma once

using namespace std;

class sortingParameters
{
	//TODO: make the variables private and add setters and getters

public:
	unsigned long long int size;
	unsigned long long int range;
	double sortPercentage;
	string dataType;
	string dataStructType;

	sortingParameters();
	~sortingParameters();
	void display();
	string toString();
};
