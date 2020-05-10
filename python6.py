# Absolute function, Round function, Ceil & Floor function, Trunc function
import math

a = abs(9)         #Absolute function gives the distance value from 0
print(a)

b = round(5.6439879, 3)     #Round function gives the value upto desired decimal point
print(b)

#import math module is mandatory for Ceil function, Floor function, Trunc function

c = math.ceil(8.4)      #Ceil function gives the greatest rounded value to the number
print(c)

d = math.floor(5.8)     #Floor function gives the lowest rounded value to the number
print(d)

e = math.trunc(35.7)        #Trunc function gives the truncated value to the number
print(e)