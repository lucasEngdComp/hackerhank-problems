#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    sum = 0
    for i in range(len(ar)):
        sum+=ar[i]
    return sum

s = simpleArraySum([1,2,3,4,5,6])
print(s)

