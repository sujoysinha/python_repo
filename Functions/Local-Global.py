a=2
def fn():
    #global a
    x= globals()['a']
    a=3
    print(a)
    print(x)
fn()
print(a)
