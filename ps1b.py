##problem set 1
##name: c4nn1b4l

#importing built in mathematical funtions
from math import *

#welcome message
print('The program that computes the sum of the logarithms of all primes from 2 to some number n.')
print('It prints out the sum of the logs of the primes, the number n, and the ratio of those two quantaties.')

#getting the number n
print("Enter the number 'n' and hit enter!")
n = input()

##initalization of state varibles
numbers = range(1,int(n))
primes = []
sum_of_the_logarithms = 0

#testing for primes and appending primes to the list named primes
for test_prime in numbers:
	iterator = 0
	divider = 1
	while (test_prime / 2) >= divider:
		if test_prime % divider == 0:
			iterator += 1
		divider += 1
	if iterator < 2:
		primes.append(test_prime)

#calculating the logs of the primes and adding them together
for prime_tobelog in primes:
	sum_of_the_logarithms = sum_of_the_logarithms + log(prime_tobelog)
	
print('Sum of the logs of the primes:', sum_of_the_logarithms)
print("The number 'n':", n)
print('The ratio between n and the sum of the logs',(float(sum_of_the_logarithms) / float(n)))
	

