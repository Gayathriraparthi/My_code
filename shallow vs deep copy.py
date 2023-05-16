import copy
l1 = [1,2,3,4,5]# copy
l2 = l1
print(l2)

l1[0] = 99
print(l1,l2)

l3 = l1.copy()# shallow copy
print(l3,l1)

l1[1] =99
print(l3,l1)

x = [[1,2,3], [0,1,2]]
x1 = x.copy()

print(x1, x)
x[1][1] = 999
print(x1, x)

x = [[1,2,3], [0,1,2]]# deep copy
x1 = copy.deepcopy(x)
print(x1, x)
x[1][1] = 999
print(x1, x)