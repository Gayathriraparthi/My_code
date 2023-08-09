l =[2,1,5,4,3,13,6,9,7,8]
#output : 5,5,13,13,13,13,9,9,8,8

for i in range(len(l)):
    max = l[0]
    for j in range(i,len(l)):
        if l[j] > l[i]:
            max = l[j]
            l[i] = l[j]
            break
print(l)