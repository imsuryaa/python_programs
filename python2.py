#local variable and global variable

def fun1():
    print('Global variable will be ' + str(a))

def fun2():
    a = 24      #local variable
    print('Local variable will be ' + str(a))
    fun1()

a = 54      #global variable
fun2()