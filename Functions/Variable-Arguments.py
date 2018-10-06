def add(farg, *args):
    sum = farg
    for i in args:
        sum+=i
    print(sum)
add(5)
add(5, 10)
add(5, 10, 15)


