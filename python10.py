# Exception Handling

try:
    n = int(input('Enter a number'))
    if num<=0:
        raise ValueError('That is not positive number')
except ValueError as error:
    print(error)