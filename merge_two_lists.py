"""Merge the following lists
given 
l1 = [1, 4, 7, 9]
l2 = [3, 8, 10]
output = [1, 3, 4, 7, 8, 9, 10]"""

#method1:
l1 = [1, 4, 7, 9]
l2 = [3, 8, 10]
output = sorted(l1 + l2)
print(output)

#method2:
l1 = [1, 4, 7, 9]
l2 = [3, 8, 10]

output = l1.copy()

output.extend(l2)
    
output = sorted(output)    
print(output)


#method3: without sort() function

l1 = [1, 4, 7, 9]
l2 = [3, 8, 10]
l = (l1 + l2)

for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[i] > l[j]:
            l[i],l[j] = l[j],l[i]
    
print(l)   