
#include "pch.h"
#include "stdafx.h"

#include "QuickSort.h"

QuickSort::QuickSort()
{

}

void QuickSort::swap(unsigned long int* a, unsigned long int* b)
{
	unsigned long int t = *a;
	*a = *b;
	*b = t;
}

int QuickSort::partition(vector<unsigned long int>& vec, int l, int r)
{
	int pivot = vec[r];    // pivot
	int i = (l - 1);  // Index of smaller element

	for (int j = l; j <= r - 1; j++)
	{
		// If current element is smaller than or
		// equal to pivot
		if (vec[j] <= pivot)
		{
			i++;    // increment index of smaller element
			swap(&vec[i], &vec[j]);
		}
	}
	swap(&vec[i + 1], &vec[r]);
	return (i + 1);
}

void QuickSort::Sort(vector<unsigned long int>& vec, int l, int r)
{
	if (l < r)
	{
		/* pi is partitioning index, arr[p] is now
		   at right place */
		int pi = partition(vec, l, r);

		// Separately sort elements before
		// partition and after partition
		Sort(vec, l, pi - 1);
		Sort(vec, pi + 1, r);
	}
}