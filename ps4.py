# Problem Set 4
# Name: c4nn1b4l


#
# Problem 1
#
#salary: the amount of money you make each year.
#save: the percent of your salary to save in the investment account each year (an integer between 0 and 100).
#growthRate: the annual percent increase in your investment account (an integer between 0 and 100).
#years: the number of years to work.
#return: a list whose values are the size of your retirement account at the end of each year.

def nestEggFixed(salary, save, growthRate, years):
	if not isinstance(salary,int) or not isinstance(save,int) or not isinstance(growthRate,int) or not isinstance(years,int):
		return None
	elif save < 0 or save > 100:
		return None
	else:
		savings = []
		ay_savings = 0.00
		for ay in range(years):
			if len(savings) == 0:
				ay_savings = (salary * save * 0.01)
				savings.append(ay_savings)
			else:
				ay_savings = savings[-1] * (1 + 0.01 * growthRate) + (salary * save * 0.01)
				savings.append(ay_savings)
		return savings

		
#problem 1's test
def testNestEggFixed():
	salary     = 10000
	save       = 10
	growthRate = 15
	years      = 5
	savingsRecord = nestEggFixed(salary, save, growthRate, years)
	print(savingsRecord)


#
# Problem 2
#
#salary: the amount of money you make each year.
#save: the percent of your salary to save in the investment account each year (an integer between 0 and 100).
#growthRate: a list of the annual percent increases in your investment account (integers between 0 and 100).
#return: a list of your retirement account value at the end of each year.

def nestEggVariable(salary, save, growthRates):
	if not isinstance(salary,int) or not isinstance(save,int) or not isinstance(growthRates,list):
		return None
	elif save < 0 or save > 100:
		return None
	else:
		savings = []
		ay_savings = 0.00
		for gr in growthRates:
			if len(savings) == 0:
				ay_savings = (salary * save * 0.01)
				savings.append(ay_savings)
			else: 
				ay_savings = savings[-1] * (1 + 0.01 * gr) + (salary * save * 0.01)
				savings.append(ay_savings)
		return savings


#problem 2's test
def testNestEggVariable():
	salary      = 10000
	save        = 10
	growthRates = [3, 4, 5, 0, 3]
	savingsRecord = nestEggVariable(salary, save, growthRates)
	print(savingsRecord)


#
# Problem 3
#
#savings: the initial amount of money in your savings account.
#growthRate: a list of the annual percent increases in your investment account (an integer between 0 and 100).
#expenses: the amount of money you plan to spend each year during retirement.
#return: a list of your retirement account value at the end of each year.

def postRetirement(savings, growthRates, expenses):
	if not isinstance(growthRates,list):
		return None
	else:
		retfound = []
		ay_found = 0
		for gr in growthRates:
			if len(retfound) == 0:
				ay_found = savings * (1 + 0.01 * gr) - expenses
				retfound.append(ay_found)
			else:
				ay_found = retfound[-1] * (1 + 0.01 * gr) - expenses
				retfound.append(ay_found)
		return retfound


#problem 3's test
def testPostRetirement():
	savings     = 100000
	growthRates = [10, 5, 0, 5, 1]
	expenses    = 30000
	savingsRecord = postRetirement(savings, growthRates, expenses)
	print(savingsRecord)
	
	
#
# Problem 4
#
#salary: the amount of money you make each year.
#save: the percent of your salary to save in the investment account each year (an integer between 0 and 100).
#preRetireGrowthRates: a list of annual growth percentages on investments while you are still working.
#postRetireGrowthRates: a list of annual growth percentages on investments while you are retired.
#epsilon: an upper bound on the absolute value of the amount remaining in the investment fund at the end of retirement.

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates, epsilon):
	if not isinstance(salary,int) or not isinstance(save,int) or not isinstance(preRetireGrowthRates,list) or not isinstance(postRetireGrowthRates,list) or not isinstance(epsilon,float):
		return None
	elif save < 0 or save > 100 or epsilon < 0:
		return None
	elif (nestEggVariable(salary, save, preRetireGrowthRates))[-1] < 0:
		return None
	else:
		all_saving = nestEggVariable(salary, save, preRetireGrowthRates)[-1]
		guess_min = 0
		guess_max = all_saving + epsilon
		guess = (guess_min + guess_max) / 2
		eol_money = postRetirement(all_saving, postRetireGrowthRates, guess)[-1]
		iterator = 0
		while abs(eol_money) > epsilon and iterator <= 1000:
			if eol_money < epsilon:
				guess_max = guess
			else :
				guess_min = guess
			guess = (guess_min + guess_max) / 2
			iterator += 1
			eol_money = postRetirement(all_saving, postRetireGrowthRates, guess)[-1]
			print(guess)
		return guess


#problem 4's test
def testFindMaxExpenses():
	salary  = 10000
	save    = 10
	preRetireGrowthRates  = [3, 4, 5, 0, 3]
	postRetireGrowthRates = [10, 5, 0, 5, 1]
	epsilon = 0.01
	expenses = findMaxExpenses(salary, save, preRetireGrowthRates,postRetireGrowthRates, epsilon)
	print('expenses:',expenses)
	
	
testFindMaxExpenses()