#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
def fizzBuzz(n) -> int:
        
    #loop for n+1 to consider the nth case    
    for i in range(1, n+1):
        
        #i mod 3 for Fizz
        if i%3==0:
            print("Fizz", end="")
            # if also mod 5 print Buzz
            if i%5==0:
                print("Buzz", end="")
            
        #i mod 5 for Buzz
        elif i%5==0:
            print("Buzz", end="")
            
        #else print number 
        else:
            print(i, end="")
        
        #reset ending parameter    
        print()



if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
