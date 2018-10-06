a,b=[int(x) for x in input('Enter two numbers: ').split()]

try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print('Cannot divide by zero!')
finally:
    print('Processing ended!')
    
