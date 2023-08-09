"""Input : test_list = [6, 4, 3] 
Output : [6, 4, 3] 

Input : test_list = [-6, -4]
Output : []"""

#test_list = [6, 4, 3]
test_list = [-6, -4]


# # Method-1:using for loop and appending to new list
# res1 = []
# for i in test_list:
#     if i > 0:
#         res1.append(i)

# print(res1)

# # Method-2:using list comprehension
# res2 = []

# res2 = [i for i in test_list if i > 0]
        
# print(res2)

# # Method-3: lambda and filter
# res3 = []

# res3 = list(filter(lambda x: x > 0,test_list))

# print(res3)

# # method-4: lambda,map,starts with()
# res4 = []

# temp = list(map(str,test_list))

# for i in temp:
#     if not i.startswith('-') and i != "0":
#         res4.append(int(i))
# print(res4)


#method-5:inplace delete the negative values 
l = [6, 4, 3, -1, -5]
length = len(l)

for i in range(0,length):
    print(i)
    if l[i] < 0:
        l.remove(l[i])
        length -= 1

print(l)

# i = 0
# length = len(l)
# while length:
#     if l[i] < 0:
#         l.pop(i)
#         i += 0
#         print(length)
#         length -= 1
#     else:
#         i += 1
#     print(l)

    
    


