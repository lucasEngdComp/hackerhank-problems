#!/bin/python3

import math
import os
import random
import re
import sys
import time

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
		cmin = 0
		cmax = 0
		smax = scores[0]
		smin = scores[0]
		for i in range(1,len(scores)):
			if scores[i] > smax:
				cmax+=1
				smax = scores[i]
			elif scores[i] < smin:
				cmin+=1
				smin = scores[i]
		return [cmax,cmin]
start = time.time()
print(breakingRecords([1,2,2,3,4,5,6,7,8,8]))
end = time.time()
print(f" time is script {end-start}")
			
			
  
