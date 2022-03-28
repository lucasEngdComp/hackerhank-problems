import math
import os
import random
import re
import sys

def getTotalX(a):
    for num in range(len(a)):
        left = all([num/numA == 0 for numA in a])

    return left
    
print(getTotalX([1,1,1]))
