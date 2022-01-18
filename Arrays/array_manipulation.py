#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
  c = Counter()
  for a, b, k in queries:
    c[a] += k
    c[b+1] -= k
  
  arrSum = 0
  maxSum = 0

  for i in sorted(c)[:-1]:
    arrSum += c[i]
    if(arrSum > maxSum):
      maxSum = arrSum

  return maxSum


if __name__ == '__main__':
    n = 5
    m = 3
    # n = int(input().strip())
    # m = int(input().strip())

    queries = []

    queries.append([1,2,100])
    queries.append([2,5,100])
    queries.append([3,4,100])

    # for _ in range(m):
    #     queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print(result)
