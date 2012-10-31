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
		
		
def constrainedMatchPair(firstMatch,secondMatch,length):
	if not isinstance(firstMatch, tuple) or not isinstance(secondMatch, tuple) or not isinstance(length, int):
		return None
	else:
		ans = ()
		for n in firstMatch:
			for k in secondMatch:
				if length + n + 1 == k:
					ans += (n,)
		return ans
	
	
def subStringMatchOneSub(key,target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = []
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = list(constrainedMatchPair(match1,match2,len(key1)))
        allAnswers = allAnswers + filtered
    allAnswers = sorted(set(allAnswers))
    return tuple(allAnswers)
	
        
def subStringMatchExactlyOneSub(target,key):
	allmatches = subStringMatchOneSub(key, target)
	exactmatches = subStringMatchExact(target, key)
	answe = ()
	for item in allmatches:
		if item not in exactmatches:
			answe += (item,)
	return answe
	
		
#targets

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

print(subStringMatchExactlyOneSub(target2,key13))
