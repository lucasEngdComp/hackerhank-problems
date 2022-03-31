
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
	c=0
	for i in range(len(s)-m+1):
			if sum(s[i:i+m])==d:
				c+=1
	return c
					
result = birthday([1,1,1,1,9],4,4)
print(result)

a = sum([2 for y in range(10)])
print( a)
