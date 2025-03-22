#!/usr/bin/python3
import sys

def factorial(n):
	"""
	Computes the factorial of a given number using recursion.

	Args:
	n (int): The number to compute the factorial for.

	Returns:
	int: The factorial of n.
	"""
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)

if __name__ == "__main__":
	"""
	Main execution: Reads an integer from command-line arguments,
	calculates its factorial, and prints the result.
	"""
	f = factorial(int(sys.argv[1]))
	print(f)
