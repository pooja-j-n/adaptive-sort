
#include "stdafx.h"

#include "SortCaller.h"

using namespace std;
using namespace chrono;

SortCaller::SortCaller()
{

}

SortCaller::SortCaller(vector<unsigned long int> vec, sortingParameters param)
{
	inputVector = vec;
	inputParam = param;
}

void SortCaller::CallSortOnVector()
{
	high_resolution_clock::time_point t1, t2;
	duration<double> time_span;
	ofstream output_file;
	vector<double> time_durations;

	/******************************Merge Sort*******************************************/
	cout << "Calling Merge Sort" << std::endl;
	vector<unsigned long int> tempMergeSort = inputVector;
	MergeSort objMergeSort = MergeSort();

	t1 = high_resolution_clock::now();
	objMergeSort.Sort(tempMergeSort, 0, tempMergeSort.size() - 1);
	t2 = high_resolution_clock::now();
	time_span = duration_cast<duration<double>>(t2 - t1);
	cout << "Time taken in Merge  Sort : " << time_span.count() << " seconds." << std::endl;
	time_durations.push_back((t2 - t1).count());

	/******************************Insertion Sort*******************************************/
	cout << "Calling Insertion Sort" << std::endl;
	vector<unsigned long int> tempInsertionSort = inputVector;
	InsertionSort objInsertionSort = InsertionSort();

	t1 = high_resolution_clock::now();
	objInsertionSort.Sort(tempInsertionSort);
	t2 = high_resolution_clock::now();
	time_span = duration_cast<duration<double>>(t2 - t1);
	cout << "Time taken in Insertion  Sort : " << time_span.count() << " seconds." << std::endl;
	time_durations.push_back((t2 - t1).count());

	/******************************Quick Sort*******************************************/
	cout << "Calling Quick Sort" << std::endl;
	vector<unsigned long int> tempQuickSort = inputVector;
	QuickSort objQuickSort = QuickSort();

	t1 = high_resolution_clock::now();
	objInsertionSort.Sort(tempQuickSort);
	t2 = high_resolution_clock::now();
	time_span = duration_cast<duration<double>>(t2 - t1);
	cout << "Time taken in Quick  Sort : " << time_span.count() << " seconds." << std::endl;
	time_durations.push_back((t2 - t1).count());

	/***************************Writing to file****************************************/
	output_file.open("adaptive-sort-dataset.csv", fstream::app);
	vector<double>::iterator it = min_element(time_durations.begin(), time_durations.end());
	int class_label = distance(time_durations.begin(), it) + 1;
	output_file << inputParam.toString() << "," << class_label << endl;
	output_file.close();


}