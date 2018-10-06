map1 = {1:'India', 2:'Bangladesh', 3:'Srilanka'}

print(map1[1])

for key in map1:
    print(key)

for key, value in map1.items():
    print ('key = {} value = {}', format(key, value))