#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    aliceWinner=0
    bobWinner=0
    for i in range(3):
            if a[i] > b[i]:
                aliceWinner+=1
            if (a[i] < b[i]):  
                bobWinner+=1
    listw = [aliceWinner,bobWinner]
    return listw   

compareTriplets([1,1,1],[1,1,1])
