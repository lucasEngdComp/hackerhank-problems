#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
#[1,2,3]
#[1,6,7]

# This question not understand.

def getTotalX(a, b):
    A = max(a)
    B = min(b)
    C= 0
    for j in range(A, B + 1):
        arr1 = all([j % i == 0 for i in a])
        arr2 = all([p % j == 0 for p in b])
        C += arr1 * arr2
    return C
    
print(getTotalX([2,2,3],[2,2,2]))
 
