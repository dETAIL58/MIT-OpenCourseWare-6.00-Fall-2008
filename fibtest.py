###
### Testing Fibonacci
### <http://en.wikipedia.org/wiki/Fibonacci_number>
### By definition, the first two numbers in the Fibonacci sequence are
### 0 and 1, and each subsequent number is the sum of the previous two.
### 0 1	1 2 3 5	8 13 21 34 55 89 144
###

import time

def fib(n):
    """
    Fibonacci storing the values in a list

    n: the number of Fibonacci numbers you want, whole number
    """
    assert isinstance(n,int), "n has to be a whole number"
	
    startTime = time.time()
    
    # First two results default to 0, 1
    result = [0, 1]

    for x in range(2, n+1):
        result.append(result[x-2] + result[x-1])
        # Check to make sure we have not gone past # of seconds to calculate.
        if time.time() - startTime > 5:
            print "*** Taking longer than 5 seconds, ending ***"
            break
    endTime = time.time()
    print "%d Fibonacci numbers took %0.2f to execute." % (x, endTime - startTime)
    return result


def reFib(n):
	"""
	Fibonacci recursively
	
	n: the number of Fibonacci numbers you want, whole number
	"""
	assert isinstance(n,int), "n has to be a whole number"
	
	# For testing how many times this func is called
	global count
	count += 1
	
	if n < 2: return n
	else: return reFib(n-1) + reFib(n-2)
	
	
def fastFib(n, memo={0:0, 1:1}):
	"""
	Fast Fibonacci using Memoization
	
	n: the number of Fibonacci numbers you want, whole number
	memo: dictionary to store previous computations
	"""
	assert isinstance(n,int), "n has to be a whole number"
	
	# For testing how many times this func is called
	global count
	count += 1
	
	if n not in memo:
		memo[n] = fastFib(n-1, memo) + fastFib(n-2, memo)
	return memo[n]



###
### For testing to see the difference
###

n = 30

count = 0
print "reFib(%d) = %d, count = %d" % (n, reFib(n), count)

count = 0
print "fastFib(%d) = %d, count = %d" % (n, fastFib(n), count)
