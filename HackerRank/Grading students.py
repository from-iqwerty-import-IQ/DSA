#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    

    for i in grades:
        if i >= 38:
            
            if 5- (i % 5) < 3:
                print(i+( 5- i%5))
                
            else:
                print(i)
        else :
            
            print(i)
            
    
        

if __name__ == '__main__':
    

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

