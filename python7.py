#Modf, Power, Pi, Degree and Radians functions
import math

m = math.modf(45.86758)   #separates fractional part & integer part
print(m)

p = math.pow(5,2)       # gives the power of number
print(p)

i = math.pi        #gives the pi value
print(i)

deg = math.degrees(math.pi)     #function used to convert radians to degrees
print(deg)

rad = math.radians(180)     #function used to convert degrees to radians
print(rad)