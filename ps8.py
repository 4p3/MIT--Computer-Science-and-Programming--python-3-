# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name: c4nn1b4l


import time
import copy


SUBJECT_FILENAME = "subjects.txt"
VALUE, WORK = 0, 1


# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """
    subValWork = {}
    inputFile = open(filename)
    for line in inputFile:
        namValWor = (line.strip('/n')).split(',')
        subValWork[str(namValWor[0])] = ( int(namValWor[1]), int(namValWor[2]) )
    return subValWork


def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = list(subjects.keys())
    subNames.sort()
    for s in subNames:
        val = subjects[s][0]
        work = subjects[s][1]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print(res)


def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[0]
    val2 = subInfo2[0]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[1]
    work2 = subInfo2[1]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[0]
    val2 = subInfo2[0]
    work1 = subInfo1[1]
    work2 = subInfo2[1]
    return float(val1) / work1 > float(val2) / work2


# Problem 2: Subject Selection By Greedy Optimization
#
def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    currentWork = 0
    answer = {}
    subjectsMutable = list( subjects.keys() )
    while True:
        maxVal = ""
        #seraching for the maximum value
        for subji in subjectsMutable:
            if len(maxVal) == 0:
                maxVal = subji
            elif comparator(subjects[subji], subjects[maxVal]):
                maxVal = subji
        #ensuring not to exceed maxWork, i know it's ugly but i got frustrated over a sitcom so i just wanted to make it work, asap
        #shitty excuse is shitty
        if currentWork <= maxWork:
            if maxVal == "":
                break
            elif subjects[maxVal][1] + currentWork <= maxWork:
                answer[maxVal] = subjects[maxVal]
                subjectsMutable.remove(maxVal)
                currentWork += subjects[maxVal][1]
                #print(currentWork, answer) #debug stuff
            else:
                try:
                    subjectsMutable.remove(maxVal)
                except KeyError:
                    break
        else:
            break
    return answer


def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = list(subjects.keys())
    tupleList = list(subjects.values())
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset: 
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue


# Problem 3: Subject Selection By Brute Force
#
def timeOutHandler(signum, frame):
    raise Exception("TimedOut")

def bruteForceTime(subjects, timeOut):
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.

    timeOut: the maximum time the function waits for bruteForceAdvisor before terminating
    """
    maxWork = 0
    while True:
        maxWork += 1
        startTime = time.time()
        bruteForceAdvisor(subjects, maxWork)
        endTime = time.time()
        print('Maximum work:',maxWork,'time:',(endTime - startTime))
        if (endTime - startTime) >= timeOut:
            break

bruteForceTime(loadSubjects(SUBJECT_FILENAME), 20)

# Problem 3 Observations
# ======================
#
# Nothing particular. Tried to implement a version, where the function would have terminated the 
# bruteForceAdvisor when it reached the time limit, but i would have produced a *nix only code,
# and did not wanted to get an unportable code.
# Also bruteForceAdvisor runtime grows exponentially.

# #
# # Problem 4: Subject Selection By Dynamic Programming
# #
# def dpAdvisor(subjects, maxWork):
#     """
#     Returns a dictionary mapping subject name to (value, work) that contains a
#     set of subjects that provides the maximum value without exceeding maxWork.

#     subjects: dictionary mapping subject name to (value, work)
#     maxWork: int >= 0
#     returns: dictionary mapping subject name to (value, work)
#     """
#     # TODO...

# #
# # Problem 5: Performance Comparison
# #
# def dpTime():
#     """
#     Runs tests on dpAdvisor and measures the time required to compute an
#     answer.
#     """
#     # TODO...

# # Problem 5 Observations
# # ======================
# #
# # TODO: write here your observations regarding dpAdvisor's performance and
# # how its performance compares to that of bruteForceAdvisor.