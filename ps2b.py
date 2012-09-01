###
### template of code for Problem 4 of Problem Set 2, Fall 2008
###

bestSoFar = 0           # variable that keeps track of largest number
                        # of McNuggets that cannot be bought in exact quantity

packages = (6,9,20)     # variable that contains package sizes
n = 50                  # number of McNuggets to try
counter = 0             # counting number of matches, looking for 6 in a row

for meal in range(1, n):
    exactHit = False        # Reset state control
    
    for c in range(0,meal/packages[2]+1):
        if exactHit == True:
            break
        
        for b in range(0,meal/packages[1]+1):
            if exactHit == True:
                break
            
            for a in range(0,meal/packages[0]+1):
                if (packages[0]*a)+(packages[1]*b)+(packages[2]*c) == meal:
                    #print "EXACT: %d = %d(%d) + %d(%d) + %d(%d) COUNT:%d\n"\
                    #      % (meal,packages[0],a,packages[1],b,packages[2],c,counter+1)
                    exactHit = True
                    counter += 1        # Update counter
                    if counter == 6:
                        print "Given package sizes %d, %d, and %d, "\
                              "the largest number of McNuggets that "\
                              "cannot be bought in exact quantity is: %d"\
                              % (packages[0], packages[1], packages[2], bestSoFar) 
                        break

    if exactHit == False:
        counter = 0          # Reset counter
        bestSoFar = meal
        #print "NOT FOUND: %d = 6(%d) + 9(%d) + 20(%d)\n" % (meal,a,b,c)
