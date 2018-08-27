
#include "stdafx.h"

#include "SortCaller.h"

using namespace chrono;

SortCaller::SortCaller()
{

}

SortCaller::SortCaller(vector<unsigned long int> vec)
{
	inputVector = vec;
}

void SortCaller::CallSortOnVector()
{
	high_resolution_clock::time_point t1, t2;
	duration<double> time_span;
	/******************************Merge Sort*******************************************/
	cout << "Calling Merge Sort" << std::endl;
	vector<unsigned long int> tempMergeSort = inputVector;
	MergeSort objMergeSort = MergeSort();

	t1 = high_resolution_clock::now();
	objMergeSort.Sort(tempMergeSort, 0, tempMergeSort.size() - 1);
	t2 = high_resolution_clock::now();
	time_span = duration_cast<duration<double>>(t2 - t1);
	/*std::ofstream output_file("sorted.txt");
	std::ostream_iterator<string> output_iterator(output_file, "\n");
	for (const auto &e : temp) output_file << e << "\n";*/
	cout << "Time taken in Merge  Sort : " << time_span.count() << " seconds." << std::endl;

	/******************************Insertion Sort*******************************************/
	cout << "Calling Insertion Sort" << std::endl;
	vector<unsigned long int> tempInsertionSort = inputVector;
	InsertionSort objInsertionSort = InsertionSort();

	t1 = high_resolution_clock::now();
	objInsertionSort.Sort(tempInsertionSort);
	t2 = high_resolution_clock::now();
	time_span = duration_cast<duration<double>>(t2 - t1);
	/*std::ofstream output_file("sorted.txt");
	std::ostream_iterator<string> output_iterator(output_file, "\n");
	for (const auto &e : temp) output_file << e << "\n";*/
	cout << "Time taken in Insertion  Sort : " << time_span.count() << " seconds." << std::endl;

	/******************************Quick Sort*******************************************/
	cout << "Calling Quick Sort" << std::endl;
	vector<unsigned long int> tempQuickSort = inputVector;
	QuickSort objQuickSort = QuickSort();

	t1 = high_resolution_clock::now();
	objInsertionSort.Sort(tempQuickSort);
	t2 = high_resolution_clock::now();
	time_span = duration_cast<duration<double>>(t2 - t1);
	/*std::ofstream output_file("sorted.txt");
	std::ostream_iterator<string> output_iterator(output_file, "\n");
	for (const auto &e : temp) output_file << e << "\n";*/
	cout << "Time taken in Quick  Sort : " << time_span.count() << " seconds." << std::endl;

}