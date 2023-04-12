#include "search_algos.h"

/**
  * linear_search - linear search algorithm.
  * @array: pointer to first element in array.
  * @size: size of array.
  * @value: value to find in array.
  *
  * Return: index where value is found or (-1).
  */

int linear_search(int *array, size_t size, int value)
{
	unsigned int f;

	if (array == NULL)
		return (-1);
	for (f = 0; f < size; f++)
	{
		printf("Value checked array[%d] = [%d]\n", f, array[f]);
		if (array[f] == value)
			return (f);
	}
	return (-1);
}

