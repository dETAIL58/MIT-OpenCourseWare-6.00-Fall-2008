from math import *

# Problem Set 1
# Name: 
# Start 6:00pm
# Stop: 7:00pm
# Time: 1:00

# Problem 2 Purpose: Compute sum of log of all primes and ratio of
#                       sum and the prime, should keep getting closer to 1

prime = [2]
totalLogs = log(prime[0])

print "Total Sum of Logs:", totalLogs, " Prime:", prime[0], \
      " Ratio:", totalLogs/prime[0]

for primeCandidate in range(prime[0]+1, 1001):
    divider = 2;
    divized = 0;
    
    while divider < primeCandidate:
        if primeCandidate % divider == 0:
            divized += 1
            break
        divider += 1

    if divized == 0:            #Found a prime!
        prime.append(primeCandidate)
        totalLogs += log(prime[len(prime)-1])
        print "Total Sum of Logs:", totalLogs, " Prime:", prime[len(prime)-1], \
              " Ratio:", totalLogs/prime[len(prime)-1]
