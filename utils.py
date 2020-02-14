# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018

def f(x):
	eval(x)
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
	return racplus, racmoin

def integrate(function, lower, upper):
	deltax=0.0001
	aire=0
	x=lower
	while x < upper:
		x+=deltax
		value = eval(function)
		aire +=deltax*value
	return round(aire, 3)
		
if __name__ == "__Main__":
	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))
