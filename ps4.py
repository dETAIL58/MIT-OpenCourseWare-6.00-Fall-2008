# Problem Set 4
# Name: 
# Time: 8:30p

#
# Problem 1
#

def nestEggFixed(salary, save, growthRate, years):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: the annual percent increase in your investment account (an
      integer between 0 and 100).
    - years: the number of years to work.
    - return: a list whose values are the size of your retirement account at
      the end of each year.
    """
    assert salary > 0, "salary needs to be greater than zero"
    assert save > 0 and save <= 100, "save needs to be between 1-100"
    assert growthRate >= 0 and growthRate <= 100, "growthRate needs to be between 0-100"
    assert years > 0, "years needs to be greater than zero"

    fund = []           # where we will store the results for each year
    save /= 100.0       # turn the percentages into a decimal
    growthRate /= 100.0
    years = int(years)    # make sure we use whole years

    # Compute 1st year amount saved
    fund.append(salary * save)
    # Complete any following years adding growth of principle
    for x in range(1, years):
        fund.append(fund[x-1] * (1 + growthRate) + salary * save)
        
    return fund
        

def testNestEggFixed():
    salary     = 10000
    save       = 10
    growthRate = 15
    years      = 5
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print savingsRecord
    # Output should have values close to:
    # [1000.0, 2150.0, 3472.5, 4993.375, 6742.3812499999995]

    # TODO: Add more test cases here.

#
# Problem 2
#

def nestEggVariable(salary, save, growthRates):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: a list of the annual percent increases in your investment
      account (integers between 0 and 100).
    - return: a list of your retirement account value at the end of each year.
    """
    assert salary > 0, "salary needs to be greater than zero"
    assert save > 0 and save <= 100, "save needs to be between 1-100"
    for x in range(len(growthRates)):
        assert growthRates[x] >= 0 and growthRates[x] <= 100,\
               "growthRate needs to be between 0-100"
        growthRates[x] /= 100.0  # turn percentage into a decimal
        
    fund = []                    # where we will store the results for each year
    save /= 100.0                # turn the percentages into a decimal
    years = len(growthRates)     # number of rates = number of years

    # Compute 1st year amount saved
    fund.append(salary * save)
    # Complete any following years adding growth of principle
    for x in range(1, years):
        fund.append(fund[x-1] * (1 + growthRates[1]) + salary * save)
        
    return fund


def testNestEggVariable():
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print savingsRecord
    # Output should have values close to:
    # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]

    # TODO: Add more test cases here.

#
# Problem 3
#

def postRetirement(savings, growthRates, expenses):
    """
    - savings: the initial amount of money in your savings account.
    - growthRate: a list of the annual percent increases in your investment
      account (an integer between 0 and 100).
    - expenses: the amount of money you plan to spend each year during
      retirement.
    - return: a list of your retirement account value at the end of each year.
    """
    assert savings > 0, "savings needs to be greater than zero"
    for x in range(len(growthRates)):
        assert growthRates[x] >= 0 and growthRates[x] <= 100,\
               "growthRate needs to be between 0-100"
        growthRates[x] /= 100.0  # turn percentage into a decimal

    fund = []           # where we will store the results for each year
    years = len(growthRates)    # make sure we use whole years

    # 1st year savings
    fund.append(savings * (1 + growthRates[0]) - expenses)
    # Complete any following years adding growth of principle
    for x in range(1, years):
        fund.append(fund[x-1] * (1 + growthRates[x]) - expenses)
        
    return fund

    

def testPostRetirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print savingsRecord
    # Output should have values close to:
    # [80000.000000000015, 54000.000000000015, 24000.000000000015,
    # -4799.9999999999854, -34847.999999999985]

    # TODO: Add more test cases here.

#
# Problem 4
#

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - preRetireGrowthRates: a list of annual growth percentages on investments
      while you are still working.
    - postRetireGrowthRates: a list of annual growth percentages on investments
      while you are retired.
    - epsilon: an upper bound on the absolute value of the amount remaining in
      the investment fund at the end of retirement.
    """
    # How much money will I have when I retire?
    fund = nestEggVariable(salary, save, preRetireGrowthRates)
    # Figure out how much can I spend
    # Number of postRetireGrowthRates = number of years I plan to be retired

    # First expense guess is the middle of range(0, savings+epsilon)
    high, low = fund[-1], 0
    expenses = (fund[-1] + epsilon) / 2
    
    for x in range(100):
        postFund = postRetirement(fund[-1], postRetireGrowthRates, expenses)
        print "%d) Estimate of expenses: %f" % (x, expenses)
        #print "%f is left after %d years of retirement" % (postFund[-1], len(postRetireGrowthRates))

        # Too much left over, need to increase expenses
        if postFund[-1] > epsilon:
            low = expenses
            expenses = (expenses + high) / 2
        # Expenses are too high, need to decrease expenses
        elif postFund[-1] < -1 * epsilon:
            high = expenses
            expenses = (expenses + low) / 2
        else: return expenses
    return None



def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print expenses
    # Output should have a value close to:
    # 1229.95548986

    # TODO: Add more test cases here.
    salary                = 180000
    save                  = 15
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [3, 3, 0, 3, 1]
    epsilon               = 10
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print expenses
