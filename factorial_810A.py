import unittest

def factorial(n):
	""" return n! using a recursive solution"""
	if n==1:
		return 1
	else:
		return n-1

if __name__ == "__main__":
	unittest.main(exit=False)