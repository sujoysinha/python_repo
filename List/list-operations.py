x = [10, 20, 30, 30, 50]
'''number of occurrances of a number'''
n = x.count(30)
print(n)
'''finding common elements in two list'''
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [5,6,7]

list3 = set(list1).intersection(set(list2))
print(list3)

a = [1,2]
b = [a, 3,4,5]
print(b)

twoDMatrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(twoDMatrix)

for  i in twoDMatrix :
    print(i[0])

