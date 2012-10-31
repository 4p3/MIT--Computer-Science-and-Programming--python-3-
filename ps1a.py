##problem set 1
##name: c4nn1b4l

##initalization of state varibles
numbers = range(1,8000)
primes = []

#testing for primes and appending primes to the list
for test_prime in numbers:
	iterator = 0
	divider = 1
	while (test_prime / 2) >= divider:
		if test_prime % divider == 0:
			iterator += 1
		divider += 1
	if iterator < 2:
		primes.append(test_prime)
#printing out the 1000th prime
print(primes[1000])
	

