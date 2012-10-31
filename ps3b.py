#problem set 3
#name: c4nn1b4l

#enabling python string functions
from string import *


#a function that shouldreturn a tuple of the starting points of matches of the key string in the target string
def subStringMatchExact(target, key):
	if not isinstance(target, str) or not isinstance(key, str):
		return None
	elif target.count(key) == 0:
		return None
	else:
		answer = ()
		point = 0
		count = target.count(key)
		for i in range(0, count):
			point = target.find(key, point) + len(key)
			answer += ((point-len(key)),)
		return answer
	

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'