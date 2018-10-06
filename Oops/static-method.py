class MyClass:
    n=0

    def __init__(self):
        MyClass.n=MyClass.n+1

    @staticmethod
    def getObjectCount():
        print('No of objects created: ', MyClass.n)

o1=MyClass()
o2=MyClass()
o3=MyClass()
o4=MyClass()

MyClass.getObjectCount()
