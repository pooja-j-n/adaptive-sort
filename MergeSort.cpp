
#include "pch.h"
#include "stdafx.h"

#include "MergeSort.h"

MergeSort::MergeSort()
{

}

void MergeSort::SortFunc(vector<unsigned long int>& vec, int l, int m, int r)
{
	int i, j, k;
	int n1 = m - l + 1;
	int n2 = r - m;

	/* create temp arrays */
	vector<unsigned long int> vec1, vec2;

	/* Copy data to temp arrays L[] and R[] */
	for (i = 0; i < n1; i++)
		vec1.push_back(vec[l + i]);
	for (j = 0; j < n2; j++)
		vec2.push_back(vec[m + 1 + j]);

	/* Merge the temp arrays back into arr[l..r]*/
	i = 0; // Initial index of first subarray
	j = 0; // Initial index of second subarray
	k = l; // Initial index of merged subarray
	while (i < n1 && j < n2)
	{
		if (vec1[i] <= vec2[j])
		{
			vec[k] = vec1[i];
			i++;
		}
		else
		{
			vec[k] = vec2[j];
			j++;
		}
		k++;
	}

	/* Copy the remaining elements of L[], if there
	   are any */
	while (i < n1)
	{
		vec[k] = vec1[i];
		i++;
		k++;
	}

	/* Copy the remaining elements of R[], if there
	   are any */
	while (j < n2)
	{
		vec[k] = vec2[j];
		j++;
		k++;
	}
}

void MergeSort::Sort(vector<unsigned long int>& vec, int l, int r)
{
	if (l < r)
	{
		// Same as (l+r)/2, but avoids overflow for
		// large l and h
		int m = l + (r - l) / 2;

		// Sort first and second halves
		Sort(vec, l, m);
		Sort(vec, m + 1, r);

		SortFunc(vec, l, m, r);
	}
}