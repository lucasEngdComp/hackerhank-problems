#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

#Counter faz a frequencia dos numeros, ex: 9,9,9. Ele transforma em um
#dicionário e diz 9:3, ou seja, o 9 ocorreu 3 vezes.

def missingNumbers(arr, brr):
	c1 = Counter(arr)
	print(f"c2 {c1}")
	c2 = Counter(brr)
	print(f"c2 {c2}")
	c = c2-c1
	return sorted(c.keys())
	
print(missingNumbers([1,2,3,4],[1,2,3,3,5,6,7,8,9,6,3,2]))
