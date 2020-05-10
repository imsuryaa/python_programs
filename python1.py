#example for funtions
#finding an average of 3 numbers using functions by taking user input

def avg(n1, n2, n3):    #defining a function
    return (n1+n2+n3)/3.0

print("Welcome to functions, Please enter numbers below")
a = int(input("1st Value "))
b = int(input("2nd Value "))
c = int(input("3rd Value "))

result = avg(a, b, c) #function calling

print('The average of 3 numbers is ' + str(result))