#problem set 3
#name: c4nn1b4l

#enabling python string functions
from string import *

def countSubStringMatch(target, key):
	if not isinstance(target, str) or not isinstance(key, str):
		return None
	elif str.find(target, key) == -1:
		return 0
	else:
		return target.count(key)


def countSubStringMatchRecursive (target, key): 
	if not isinstance(target, str) or not isinstance(key, str):
		return None
	elif str.find(target, key) == -1:
		return 0
	else:
		if str.find(target, key) != -1:
			return ( 1 + countSubStringMatchRecursive(target[ ( str.find(target, key) + len(key)) : ], key) )
		else:
			return None
			