#Exception Handling

import math

n = int(input('Enter a number to find factorial: '))
try:
    res = math.factorial(n)
    print(res)
except:
    print('Please enter value greater than 0')