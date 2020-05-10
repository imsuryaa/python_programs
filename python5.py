#Example for variable length arguments

def func(*mylist):  #defining a function without length of arguments
    for x in mylist:
        print(x)
    return
#main
print('If we enter 3 elements in the argument')
func(12,34,56)

print('If we enter 6 elements in the argument')
func(23,65,12,65,78,90)

print('If we enter 1 element in the argument')
func(67)