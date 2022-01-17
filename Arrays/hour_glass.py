#!/bin/python3

import math
import os
import random
import re
import sys
from array import *

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    row_repeat_count = 4
    col_repeat_count = 4
    max = -sys.maxsize - 1

    for i in range(row_repeat_count):
      for j in range(col_repeat_count):
        total = 0
        starting_row_index = i
        selected_array = []
        for row in arr[starting_row_index:starting_row_index+3]:
          starting_col_count = j
          for col in row[starting_col_count:starting_col_count+3]:
            selected_array.append(col)

        total = sum(selected_array)
        total = total - (selected_array[3] + selected_array[5])
        if(total > max):
          max = total;
          max_array = selected_array
          # print("max_array", max_array)
          # print("max", max)
    return max

if __name__ == '__main__':

    arr =  [
      [-1, -1, 0, -9, -2, -2],
      [-2, -1, -6, -8, -2, -5],
      [-1, -1, -1, -2, -3, -4],
      [-1, -9, -2, -4, -4, -5],
      [-7, -3, -3, -2, -9, -9],
      [-1, -3, -1, -2, -4, -5]
    ]

    result = hourglassSum(arr)
    print(result)
