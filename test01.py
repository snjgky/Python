# -*-coding:utf_8-*-
import math

n = 18
list = []
for x in range(2,int(math.sqrt(2*n))):
    list.append(x*x)
print list

# generate the dict
dict = {}
for i in range(1,n+1):
    result = []
    for j in range(len(list)):
        if list[j]-i>0 and list[j]-i<n+1 and list[j]-i!=i:
            result.append(list[j]-i)
    dict[i] = result

# remove value in dict
def remove_value(dict,key1,value1):
    for key,value in dict.items():
        if key == key1:
            continue
        elif key == value1:
            dict[value1] = [key1]
        elif value1 in value:
            dict[key].remove(value1)
    return dict

print dict

temp = set()
while len(temp)<n:
    for key,value in dict.items():
        if key in temp:
            continue
        elif len(value)==1:
            temp.add(key)
            temp.add(value[0])
            dict = remove_value(dict,key,value[0])

print(len(temp))
print dict[1]
print(dict)
