int rand()
{
	static int i;
	int numz[] = {8, 8, 7, 9, 23, 74};

	return numz[i++ %6];
}
