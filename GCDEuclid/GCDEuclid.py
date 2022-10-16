"""
Created on Sat Oct 15 16:54:58 2022

@author: okroe

My Own Work
"""

import random

def findGCD(A, B):
    
    # variables
    newA = 0
    newB = 0
    temp = 0
    
    # set the higher variable to newA, lower to newB
    if(A > B):
        newA = A
        newB = B
    else:
        newA = B
        newB = A
    
    # Greatest Common Denominator
    GCD = 1
    
    # is GCD found
    GCD_found = False

    # while GCD has not been found
    while(GCD_found != True):
        
        # if newA = 0, newB is the GCD
        if(newA == 0):
            GCD = newB
            GCD_found = True
            
        # if newB = 0, newA is the GCD
        elif(newB == 0):
            GCD = newA
            GCD_found = True
            
        # temp = orig newA, newA = newB, newB = remainder of orig newA / newB
        else:
            temp = newA
            newA = newB
            newB = temp % newB
    
    print("GCD is " + str(GCD))
    

# function to run 100 random numbers through findGCD function
def genNumbersGCD():
    
    # 100 times
    for i in range(100):
        # generate two random numbers
        randNum1 = random.randrange(0, 999999)
        randNum2 = random.randrange(0, 999999)
        
        # pass random numbers into GCD function        
        findGCD(randNum1, randNum2)

genNumbersGCD()