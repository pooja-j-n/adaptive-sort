
#include "pch.h"
#include "stdafx.h"

#include "InsertionSort.h"

InsertionSort::InsertionSort()
{

}

void InsertionSort::Sort(vector<unsigned long int>& vec)
{
	int i, key, j;
	int n = vec.size();
	for (i = 1; i < n; i++)
	{
		key = vec[i];
		j = i - 1;

		/* Move elements of arr[0..i-1], that are
		   greater than key, to one position ahead
		   of their current position */
		while (j >= 0 && vec[j] > key)
		{
			vec[j + 1] = vec[j];
			j = j - 1;
		}
		vec[j + 1] = key;
	}
}