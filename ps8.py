# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#

import time

# creating a small catalog to test with
##fo = open('smallCatalog.txt', 'w')
##fo.write("6.00,16,8\n1.00,7,7\n6.01,5,3\n15.01,9,6")
##fo.close()

##SUBJECT_FILENAME = "smallCatalog.txt"
SUBJECT_FILENAME = "subjects.txt"
VALUE, WORK = 0, 1

#
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
    dict = {}
    inputFile = open(filename)
    for line in inputFile:
        list = line.strip().split(',')
        dict[list[0]] = (int(list[1]), int(list[2]))
    inputFile.close()
    return dict


def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res


def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2

#
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
    if len(subjects) == 0:
        return 'Empty SubjectList'
    assert(maxWork >= 0), "No hours of work"
    assert(comparator is cmpValue or comparator is cmpWork or comparator is cmpRatio), "Not a valid comparator." 
    
    result = {}
    totalWork = 0

    if comparator is cmpValue:
        sortedSubjects = sorted(subjects.iteritems(), key=lambda (k,v): v[VALUE], reverse=True)
    elif comparator is cmpWork:
        sortedSubjects = sorted(subjects.iteritems(), key=lambda (k,v): v[WORK])
    elif comparator is cmpRatio:
        sortedSubjects = sorted(subjects.iteritems(), key=lambda (k,v): float(v[VALUE]) / v[WORK], reverse=True)
    else: print "Not a valid comparator."

    for x in range(len(sortedSubjects)):
        if sortedSubjects[x][1][WORK] + totalWork <= maxWork:
            totalWork += sortedSubjects[x][1][WORK]
            result[sortedSubjects[x][0]] = (sortedSubjects[x][1][VALUE], sortedSubjects[x][1][WORK])
            if totalWork == maxWork: break
    return result


##
##  The old way using the cmpFunctions that came with the problem set,
##  before I learned the cool sorted and lambda functions.
##  Uncomment out the below code and comment out the code above to use.
##
##    resultUpdated = True
##    subNames = subjects.keys()
##
##    while resultUpdated:
##        resultUpdated = False
##        for x in subNames:
##            greater = False
##            if subjects[x][WORK] + totalWork <= maxWork:
##                for y in subNames:
##                    if result.get(y,'0') == '0' and subjects[y][WORK] + totalWork <= maxWork:
##                        if comparator((subjects[x][VALUE], subjects[x][WORK]), (subjects[y][VALUE], subjects[y][WORK])):
##                            greater = True
##                        elif comparator is cmpValue and subjects[x][VALUE] == subjects[y][VALUE]:
##                            greater = True
##                        elif comparator is cmpWork and subjects[x][WORK] == subjects[y][WORK]:
##                            greater = True
##                        elif comparator is cmpRatio and float(subjects[x][VALUE]) / subjects[x][WORK] == float(subjects[y][VALUE]) / subjects[y][WORK]:
##                            greater = True
##                        elif subjects[x] is not subjects[y]:
##                            greater = False
##                            break
##                if greater:
##                    totalWork += subjects[x][WORK]
##                    result[x] = (subjects[x][VALUE], subjects[x][WORK])
##                    resultUpdated = True
##    return result
            

def greedyAdvisorTime():
    """
    Runs tests on greedyAdvisor and measures the time required to compute
    an answer.
    """
    subjects = loadSubjects(SUBJECT_FILENAME)
    printSubjects(subjects)
    print "------------------------------\n" * 2

    for maxWork in range(1,100):
        start = time.time()
        selected = greedyAdvisor(subjects, maxWork, cmpValue)
        end = time.time()
        printSubjects(selected)
        print "maxWork: %d\tTime Spent: %0.2f" % (maxWork,end-start)
        print "------------------------------\n"
        if end - start > 5:
            print "The last greedy attempt took longer than 5 seconds, aborting..."
            break

    
def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = subjects.keys()
    tupleList = subjects.values()
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

#
# Problem 3: Subject Selection By Brute Force
#
def bruteForceTime():
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    subjects = loadSubjects(SUBJECT_FILENAME)
    printSubjects(subjects)
    print "------------------------------\n" * 2

    for maxWork in range(1,11):
        start = time.time()
        selected = bruteForceAdvisor(subjects, maxWork)
        end = time.time()
        printSubjects(selected)
        print "maxWork: %d\tTime Spent: %0.2f" % (maxWork,end-start)
        print "------------------------------\n"
        if end - start > 5:
            print "The last bruteForce attempt took longer than 5 seconds, aborting..."
            break

# Problem 3 Observations
# ======================
#
# TODO: write here your observations regarding bruteForceTime's performance

#
# Problem 4: Subject Selection By Dynamic Programming
#
def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...

#
# Problem 5: Performance Comparison
#
def dpTime():
    """
    Runs tests on dpAdvisor and measures the time required to compute an
    answer.
    """
    # TODO...

# Problem 5 Observations
# ======================
#
# TODO: write here your observations regarding dpAdvisor's performance and
# how its performance compares to that of bruteForceAdvisor.


