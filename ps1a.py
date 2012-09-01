# Problem Set 1
# Name: 
# Start 5:30pm
# Stop: 6:00pm
# Time: 0:30

# Problem 1 Purpose: Find all the prime numbers < 1001

prime = [2]

print prime[0],

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
        print ',', prime[len(prime)-1],
