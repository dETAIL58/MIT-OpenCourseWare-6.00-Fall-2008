import time

# GLOBALS
WORK = [3,1,2,4,6,7,3,2,8,3,7,9,0,3,6,7,2,1,6,12,3,6,7,8,9,4,1,2,3,7,7,2,1,6,12,3,6,7,8,9,4,1,2,3,7]
VALUE = [7,2,1,6,12,3,6,7,8,9,4,1,2,3,7,7,2,1,6,12,3,6,7,8,9,4,1,2,3,7,7,2,1,6,12,3,6,7,8,9,4,1,2,3,7]
N = len(WORK) - 1
MEMO = dict()


def ks(aWork, i):
	"""
	knapsack using brute force method, to get the optimal value for available work.
	
	aWork: how much work we have available
	i: index to check
	"""
	# Used only for testing how many calls
	global numOfSteps
	numOfSteps += 1
	
	# Are we finished checking all options
	if i > N: return 0
	
	# If this is more work than we can fit, skip to the next option
	if aWork < WORK[i]:
		return ks(aWork, i+1)
	else:
		# Which is the optimal value, the next option or keeping this option?
		return max(ks(aWork, i+1), VALUE[i] + ks(aWork-WORK[i], i+1))
		
###
###

def ksFast(aWork, i):
	"""
	knapsack using dynamic programming (memoization), to get the optimal value 
	for available work.
	
	aWork: how much work we have available
	i: index to check
	"""
	# Used only for testing how many calls
	global numOfSteps
	numOfSteps += 1
	
	# Are we finished checking all options
	if i > N: return 0
	
	# Did we already compute and store the value?
	try: return MEMO[(aWork, i)]
	
	# Don't have the value stored, so do the work and store the value
	except KeyError:		
		# If this option is more work than we can fit, skip to the next option
		if aWork < WORK[i]:
			# The available work and this index will not fit
			# Skipping to the next option
			MEMO[(aWork, i)] = ksFast(aWork, i+1)
			return MEMO[(aWork, i)]
		else:
			# It fits!
			# But is the optimal choice?  Let's check:
			nextOption = ksFast(aWork, i+1)
			keepThisOption = VALUE[i] + ksFast(aWork-WORK[i], i+1)

			# Which is optimal and lets save it
			MEMO[(aWork, i)] = max(nextOption, keepThisOption)
			return MEMO[(aWork, i)]
		
###
###
availWork = 20
numOfSteps = 0

startTime = time.time()
print "\nks(%d) = %d, %d steps, and took %0.02f seconds" \
% (availWork, ks(availWork,0), numOfSteps, time.time() - startTime)

numOfSteps = 0
startTime = time.time()
print "\nksFast(%d) = %d, %d steps, and took %0.02f seconds" \
% (availWork, ksFast(availWork,0), numOfSteps, time.time() - startTime)