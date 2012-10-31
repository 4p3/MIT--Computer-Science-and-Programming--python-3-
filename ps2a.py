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
exercise = range(1,100)
largest_d = 0


#solving the equation
for n in exercise:
	if ((n % 6) == 0) or ((n % 9) == 0) or ((n % 20) == 0):
		buy = 1
	else:
		factors = range(0,(n+1))
		buy = 0
		for a in factors:
			for b in factors:
				for c in factors:
					if ((6 * a) + (9 * b) + (20 * c)) == n:
						buy = 1
	if buy == 0:
		largest_d = n

#printing out
print("Largest number of McNuggetsthat cannot be bought in exact quantity: ", largest_d)
	
