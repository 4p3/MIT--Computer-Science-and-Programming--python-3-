# problem set 2
# name: c4nn1b4l

# Solving a Diophantine Equation
# An iterative program that finds the largest number of McNuggetsthat cannotbe bought in exact quantity

#initalizin state varibles
a = 0
b = 0
c = 0
buy = 0
factors = []
exercise = range(1,200)
bestSoFar = 0     
packages = ()
pack_a = 0
pack_b = 0
pack_c = 0

#requesting package sizes
while pack_a <= 0:
	print('Give me the size of "a" package, and hit enter!')
	pack_a = int(input())
while pack_b <= 0:
	print('Give me the size of "b" package, and hit enter!')
	pack_b = int(input())
while pack_c <= 0:
	print('Give me the size of "c" package, and hit enter!')
	pack_c = int(input())
	
packages = pack_a, pack_b, pack_c

#solving the equation
for n in exercise:
	if ((n % int(packages[0])) == 0) or ((n % int(packages[1])) == 0) or ((n % int(packages[2])) == 0):
		buy = 1
	else:
		factors = range(0,(n+1))
		buy = 0
		for a in factors:
			for b in factors:
				for c in factors:
					if ((int(packages[0]) * a) + (int(packages[1]) * b) + (int(packages[2]) * c)) == n:
						buy = 1
	if buy == 0:
		bestSoFar = n

#printing out
print("Given package sizes ",packages[0],', ',packages[1],', and ',packages[2], ', the largest number of McNuggetsthat cannot be bought in exact quantity is: ', bestSoFar)
	
