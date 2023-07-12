# num = int(input('enter number:'))
# i = 1 # start
# c = 0   # to count no.of factors
# iterations = 0 # to count iteration 
# while i <= num: # end
#     if num % i == 0:
#         c += 1
#     i += 1 # step count
#     iterations += 1

# if c <= 2:
#     print('Prime')
# else:
#     print('Not Prime')
# print('no.of iterations',iterations)  # here Order of complexity is O(n)

# num = int(input('enter number:'))
# i = 1 # start
# c = 0  # to count no.of factor
# iterations = 0  # to count iteration
# while i <= int(num/2): # end and checking num/2 as factor are only upto num/2 ,dec no.of iterations to half
#     if num % i == 0:
#         c += 1
#     i += 1
#     iterations += 1

# if c <= 2:
#     print('Prime')
# else:
#     print('Not Prime')
    
# print('no.of iterations',iterations) #here Order of complexity is num|2
        

# num = int(input('enter number:'))
# i = 1 # start
# c = 0  # to count no.of factor
# iterations = 0  # to count iteration
# while i <= int(num/2): # end and checking num/2 as factor are only upto num/2 ,dec no.of iterations to half
#     if num % i == 0:
#         c += 1
#     i += 1
#     iterations += 1

# if c <= 2:
#     print('Prime')
# else:
#     print('Not Prime')
    
# print('no.of iterations',iterations) #here Order of complexity is num|2
        


# num = int(input('enter number:'))
# root = int(num ** .5)
# i = 2 # taking 2 as intial ,bcz 1 is factor for any number
# c = 0
# iterations = 0
# if num == 1 or num == 2:
#     print(num,' is a prime number')
# else:
#     while i <= root:
#         if num % i == 0:
#             c += 1
#             iterations += 1
#             break
#         i += 1
    
#     if c == 0:
#         print('Prime')
#     else:
#         print('Not Prime')

# print('no.of iterations',iterations) #here Order of complexity is 0 or 1
        


num = int(input('enter number:'))
root = int(num ** .5)
i = 2
c = 014

iterations = 0
if num == 1 or num == 2:
    print(num,' is a prime number')
else:
    while i <= root:
        if num % i == 0:
            c += 1
            iterations += 1
            print('Not prime')
            break
        i += 1
        
    else:
        print('Prime')
        
print('no.of iterations',iterations)