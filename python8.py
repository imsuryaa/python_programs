#Dictionaries

d = dict()      #function used to create empty dictionary
print(d)

days = {'day 1' : 'Monday', 'day 2' : 'Tuesday', 'day 3' : 'Wednesday'}         #User defined dictionary
print(days)

working_days = dict(days)           #Copying from one dictionary to another dictionary
print(working_days)

length = len(days)              #function used to find length of dictionary
print(length)

check = 'day 2' in days         #used to check wheather the key value in dictionary or not
print(check)