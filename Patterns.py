#patterns
'''Write a program to print the Floyd’s triangle.
1
2 3
4 5 6
7 8 9 10'''
x = 0
for i in range(1,5):
    for j in range(0,i):
        x += 1
        print(x,end = ' ')
    print('\n')
        

'''86. Write a program to print the following triangle.
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5'''

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end = ' ')
    print('\n')
    

'''87. Write a program to print the following triangle.
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5 '''

for i in range(1,6):
    for j in range(i):
        print(i,end = ' ')
    print('\n')


'''Write a program to print the following triangle.
1
1 1
1 2 1
1 2 3 1
1 2 3 4 1
1 2 3 4 5 1'''

for i in range(1,7):
    for j in range(1,i):
        print(j,end=" ")
    print('1')
    print()
               

'''Write a program to print the following triangle.
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1'''

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j, end = ' ')
    print('\n')


'''Write a program to print the following triangle.
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5'''

for i in range(1,6):
    for j in range(5,i-1,-1):
        print(i,end = ' ')
    print('\n')
    

'''Write a program to print the following triangle.
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
'''
for i in range(5,0,-1):
    for j in range(0,i):
        print(i,end = ' ')
    print('\n')


'''Write a program to print the following triangle
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5'''

for i in range(0,5):
    for j in range(5,i,-1):
        print(j, end = ' ')
    print('\n')
    

'''93. Write a program to print the following triangle
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1'''

for i in range (5,0,-1):
    for j in range(5,i-1,-1):
        print(j,end = ' ')
    print('\n')

'''Write a program to print the following triangle.
1 1 1 1 1
  2 2 2 2
    3 3 3
      4 4
        5'''

for row in range(1,6):
    for  column in range(1,6):
        if row > column:
            print(' ',end = ' ')
        else:
            print(row,end = ' ')
    print('\n')


''' Write a program to print the following triangle.
1 2 3 4 5
  1 2 3 4
    1 2 3
      1 2
        1'''

for row in range(1,6):
    i = 0
    for column in range(1,6):
        if row > column:
            print(' ',end = ' ')
        else:
            i += 1
            print(i,end = ' ')
    print('\n')
        

'''96. Write a program to print the following triangle.
1 2 3 4 5
  2 3 4 5
    3 4 5
      4 5
        5'''

for  row in range(1,6):
    for column  in range(1,6):
        if row > column:
            print(' ',end = ' ')
        else:
            print(column,end = ' ')
    print('\n')

'''Write a program to print the following triangle.
         1
       1 2
     1 2 3
   1 2 3 4
 1 2 3 4 5
'''

for row in range(5,0,-1):
    i = 0
    for column in range(1,6):
        if row > column:
            print(' ',end = ' ')
        else:
            i += 1
            print(i,end = ' ')
    print('\n')

'''98. Write a program to print the following triangle.
1 2 3 4 5
  2 3 4 5
    3 4 5
      4 5
        5'''

for row in range(1,6):
    for  column in range(1,6):
        if row > column:
            print(' ',end = ' ')
        else:
            print(column,end= ' ')
    print('\n')

'''9. Write a program to print the following triangle.
5 4 3 2 1
  5 4 3 2
    5 4 3
      5 4
        5'''

for row in range(5,0,-1):
    i = 6
    for column in range(5,0,-1):
        if row < column:
            print(' ',end = ' ')
        else:
            i -= 1
            print(i,end = ' ')
    print('\n')


'''100. Write a program to print the following triangle.
        5
      5 4
    5 4 3
  5 4 3 2
5 4 3 2 1'''

for row in range(5,0,-1):
    i = 6
    for column in range(1,6):
        if row > column:
            print(' ' ,end = ' ')
        else:
            i -= 1
            print(i, end = ' ')
    print('\n')

'''Write a program to print the following triangle.
        1
      2 1
    3 2 1
  4 3 2 1
5 4 3 2 1
'''

for row in range(1,6):
    for  column in range(5,0,-1):
        if column <= row :
            print(column,end = ' ')
        else:
            print(' ', end = ' ')
    print('\n')

'''102. Write a program to print the following triangle.
        5
      4 5
    3 4 5
  2 3 4 5
1 2 3 4 5'''

for column in range(5,0,-1):
    for row in range(1,6):
        if row >= column:
            print(row,end = ' ')
        else:
            print(' ',end = ' ')
    print('\n')
    

'''103. Write a program to print the following triangle.
        1
      2 2
    3 3 3
  4 4 4 4
5 5 5 5 5'''

for row in range(1,6):
    for  column in range(5,0,-1):
        if row >= column:
            print(row,end =' ')
        else:
            print(' ',end =' ')
    print('\n')
            

'''104. Write a program to print the following triangle.
5
4 4
3 3 3
2 2 2 2
1 1 1 1 1'''
for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(i,end = ' ')
    print('\n')
        
'''Write a program to print the following triangle.
        5
      4 4
    3 3 3
  2 2 2 2
1 1 1 1 1
'''
for row in range(5,0,-1):
    for column in range(1,6):
        if column >= row:
            print(row,end = ' ')
        else:
            print(' ',end = ' ')
    print('\n')

''' Write a program to print the following triangle.
5 5 5 5 5
  4 4 4 4
    3 3 3
      2 2
        1'''
for row in range(5,0,-1):
    for column in range(5,0,-1):
        if row < column:
            print(' ',end = ' ')
        else:
            print(row ,end = ' ')
    print('\n')
        

'''Write a program to print the following triangle.
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5'''
'''
****1
***1*2
**1*2*3
*1*2*3*4
1*2*3*4*5'''

for row in range(5,0,-1):
    i = 0
    for column in range(1,6):
        if row > column:
            print(' ',end = '')
        else:
            i += 1
            print(str(i) + " ",end = '')
    print('\n')
    
'''Write a program to print the following triangle.
5 5 5 5 5
 4 4 4 4
  3 3 3
   2 2
    1'''

n = 5
for row in range(n,0,-1):
    for col in range(n,0,-1):
        if col <= row:
            print(str(row) + " ",end="")
        else:
            print(" ",end="")           
    print()

'''110. Write a program to print the following.
5 5 5 5 5
 4 4 4 4
  3 3 3
   2 2
    1
   2 2
  3 3 3
 4 4 4 4
5 5 5 5 5'''

for i in range(5,0,-1):
    for j in range(5,-1,-1):
        if i <= j:
            print(" ",end ="")
        else:
            print(str(i) + " ",end ="")
    print()
for i in range(2,6):
    for j in range(5,0,-1):
        if i >= j:
            print(str(i) + " ",end ="")
        else:
            print(" ",end ="")
    print()


"""    1 
      1 2 1 
    1 2 3 2 1 
  1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1 """

rows = 6
for i in range(1, rows + 1):
    for j in range(rows-1,i-1,-1):
        print(' ',end =" ")
    for j in range(1, i - 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()


'''Write a program to print the following.
      1
     1 1
    1 2 1
   1 3 3 1
  1 4 6 4 1
1 5 10 10 5 1'''
rows = 6
for i in range(rows):
    num = 1
    for s in range(rows-1,i-1,-1):
        print(' ',end ="")
    for j in range(i+1):
        print(str(num) + " ",end = "")
        num = num * (i - j)//(j +1)
    print()
