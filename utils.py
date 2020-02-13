# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018
import scipy
import scipy.integrate
def fact(n):
	
	i=1
	factoriel = 1
	if n>0:
		while i < n:
			factoriel *=i
		return factoriel
	if n==0:
		return 1


def roots(a, b, c):
	
	
	delta = b**2 - 4*a*c
	racplus=(delta**(1/2)-b)/(2*a)
	racmoin= ((-delta**(1/2))-b)/(2*a)
	return racplus,racmoin

def integrate(function, lower, upper):
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
	return scipy.integrate.quad(eval(function),lower,upper)


if __name__ == "__Main__":
	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))
