x = [10, 20, 30, 40, 50]
'''Aliasing'''
y = x
print(y)
'''cloning'''
z = x[:]
print(z)

'''changing value of element of x'''
x[2]=35
print(x)
print(y)
print(z)

'''reverse sort'''
x.sort(reverse=True)
print(x)

