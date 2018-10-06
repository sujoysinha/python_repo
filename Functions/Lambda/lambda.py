a = lambda x: x*x

print(a(10))

mylist = [1,2,3,4,5,6,7,8,9,10]
newlist = list(map(lambda x:(x*x), mylist))
print(newlist)


