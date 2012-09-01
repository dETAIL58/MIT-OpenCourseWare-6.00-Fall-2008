from string import * 

# Problem Set 3 (Part I)
# Name: 
# Start: 3:10p
# 

def countSubStringMatch(target, key):
    start = count = -1
    while True:
        count += 1      #right away count, start = 0
        start = find(target, key, start+1)
        if start == -1: return count



def countSubStringMatchRecursive(target, key):
    def doCount(target, key, count):
        start = find(target,key)
        #print start, target, key, count
        if start == -1: return count
        else: return doCount(target[start+1:], key, count+1)
    return "No. of instances of %s in %s is %s" % (key, target, doCount(target, key, 0))

print countSubStringMatchRecursive("atgacatgcacaagtatgcat","atgc")
