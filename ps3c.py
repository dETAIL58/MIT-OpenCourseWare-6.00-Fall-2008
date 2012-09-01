from string import *

# Problem Set 3 (Part III)
# Name: 
# Start: 7:00
#

# target strings
target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings
key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'


def subStringMatchExact(target, key):
    start, result = -1, ()
    while True:
        start = find(str(target), str(key), start+1)
        if start == -1: return result
        else: result = result + (start,)


def constrainedMatchPair(firstMatch,secondMatch,length):
    result = ()
    for n in firstMatch:
        for k in secondMatch:
            if n + length + 1 == k: result = result + (n,)
    return result

def subStringMatchOneSub(key,target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        print '\nbreaking key',key,'into [',key1,',',key2,']'
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        print 'match1',match1
        print 'match2',match2
        print 'possible matches for',key1,key2,'start at',filtered
    return allAnswers


print subStringMatchOneSub(key12, target1)

##for x in range(1,3):
##    for y in range(10,14):
##        print "Target:", vars()['target'+str(x)], "Key:", vars()['key'+str(y)]
##        print subStringMatchExact(vars()['target'+str(x)], vars()['key'+str(y)]);        
##


    







            


