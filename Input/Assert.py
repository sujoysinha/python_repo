x=int(input('Enter any number: '))
try:
    assert(x>10)
    print('You entered: ', x)
except AssertionError:
    print('Cannot process a number less than 10!')