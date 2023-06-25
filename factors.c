#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
	FILE *f;
	char buf[255];
	int max = 255;
	long long int n;

	if (argc <= 1)
	{
		printf("Usage: factors <file>\n");
		exit(1);
	}

	f = fopen(argv[1], "r");
	while (fgets(buf, max, f) != NULL)
	{
		printf("%lld\n", n);
		n = atoi(buf);
	}

	fclose(f);
	return (0);
}