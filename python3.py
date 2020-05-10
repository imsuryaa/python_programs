#Updating the global variable

def func():
    global var #global is keyword to represent that var is global
    var = var + 1
    print('the updated global value', var)
    return

var = 15  
func()