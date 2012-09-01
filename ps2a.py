# Problem Set 2 (Part I)
# Name: 
# Start: 12:30a
# Stop: 1:05a
# Time: 0:35
#
# Purpose: 6a, 9b, 20c  what combinations make 50-55
# Purpose: find the largest # of McNuggets that can't
#          be bought in exact quantity

# Number of McNuggets that can't be bought in exact quantity
# Answer: 43

n = 50
match = []

for meal in range(1, n):
    exactHit = False        # Reset state control
    
    for c in range(0,meal/20+1):
        if exactHit == True:
            break
        
        for b in range(0,meal/9+1):
            if exactHit == True:
                break
            
            for a in range(0,meal/6+1):
                if (6*a)+(9*b)+(20*c) == meal:
                    #print "EXACT: %d = 6(%d) + 9(%d) + 20(%d)\n" % (meal,a,b,c)
                    exactHit = True
                    match.append(meal)        # Save
                    if len(match) == 6:
                        print "Largest number of McNuggets that "\
                              "cannot be bought in exact quantity:", match[0] - 1
                        break

    if exactHit == False:
        match = []          # Reset counter
        #print "NOT FOUND: %d = 6(%d) + 9(%d) + 20(%d)\n" % (meal,a,b,c)
