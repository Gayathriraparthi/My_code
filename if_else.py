# Write a program to read the marks of 3 subjects and display the total, average,class.
telugu = float(input('enter the telugu marks:'))
english = float(input('enter the english marks:'))
hindi = float(input('enter the hindi marks:'))
total = telugu + english + hindi
average = (total)/ 3

if average < 40 and average >= 0 :
    class_ = 'fail'
elif average >= 40 and average < 65:
    class_ = 'third'
elif average >= 65 and average < 80:
    class_ = 'second'
elif average >= 80 and average < 101:
    class_ = 'first'
else:
    class_ = 'invalid input'
    
print(class_)   
    

# Write a program to check whether the given number is positive or negative.
num = float(input('enter any number: '))
if num > 0:
    print(f' {num} is positive')
elif num < 0:
    print(f' {num} is negative')
else:
    print(f'{num} is neither positive nor negative ')

# Write a program to find out the given number is odd or even.
num = int(input('enter any number: '))
if num % 2 == 0:
    print(f' {num} is even')
else:
    print(f' {num} is odd')

# Write a program to find smallest of given two numbers.
a = int(input('enter number:'))
b = int(input('enter number:'))
if a < b :
    print(f'{a} is smaller than {b}')
elif b < a:
    print(f'{b} is smaller than {a}')
    

# Write a program to find biggest of given three numbers.
x = int(input('enter x number:'))
y = int(input('enter y number:'))
z = int(input('enter z number:'))
if x > y and x > z:
    print(f'{x} is greater than {y},{z}')
elif y > x and y > z:
    print(f'{y} is greater than {x},{z}')
else:
    print(f'{z} is greater than {y},{x}')


# Write a program to check whether the given year is leap year or not.
year = int(input('enter year:'))
if year % 4 == 0:
    print(f'{year} is leap year')
else:
    print(f'{year} is not leap year')


# Write a program to find the roots of a given quadratic equation and print the nature of roots.

b = 5 ; c = 6 ; a = 1

d = (b**2) - (4 * a * c)

x1 = (-b + (b**2 - (4*a*c))) / 2 * a
x2 = (-b - (b**2 - (4*a*c))) / 2 * a

print(x1,x2)

if d > 0:
    print('real and distinct')
elif d == 0:
    print('real and equal')
elif d < 0:
    print('complex and distinct')


# Write a program to read three sides a, b, c of a triangle and print the type of the triangle.
a = int(input("Enter side a "))
b = int(input("Enter side b "))
c = int(input("Enter side c "))

if a == b == c:
    print('equilateral')
elif a == b or b == c or a == c:
    print('isosceles')
elif a != b != c:
     print('sacalene')
    


'''Write a program to calculate the monthly income of a person using the
following commission schedule:
Monthly sales income
>= Rs.50,000 Rs.375 + 16% sales.
>= Rs.50,000 but >=Rs.40,000 Rs. 350+14% sales.
<= Rs.40,000 but >=Rs.30,000 Rs. 325+12% sales.
<= Rs.30,000 but >=Rs.20,000 Rs. 300+9% sales.
<= Rs.20,000 but >=Rs.10,000 Rs. 250+5% sales.
<= Rs.10,000 Rs. 200+3% sales.'''

Monthly_sales_income = float(input('enter monthly sales income:'))


if Monthly_sales_income >= 50000:
    income = (375 * 30) + (Monthly_sales_income * 0.16)
elif Monthly_sales_income < 50000 and Monthly_sales_income >= 40000:
    income = (350 * 30) + (Monthly_sales_income * 0.14)
elif Monthly_sales_income < 40000 and Monthly_sales_income >= 30000:
    income = (325 * 30) + (Monthly_sales_income * 0.12)
elif Monthly_sales_income < 30000 and Monthly_sales_income >= 20000:
    income = (300 * 30) + (Monthly_sales_income * 0.09)
elif Monthly_sales_income < 20000 and Monthly_sales_income >= 10000:
    income = (250 * 30) + (Monthly_sales_income * 0.05)
elif Monthly_sales_income <= 20000 and Monthly_sales_income > 0 :
    income = (200 * 30) + (Monthly_sales_income * 0.03)
else:
    income = 'enter valid data'
print(income)
    


'''Write a program to read a 3-digit number and find whether the middle digit is
numerically equal to the sum of the other two digits and prints an appropriate
response.'''
num = input('enter 3 digit number:')

if int(num[1]) == int(num[0]) + int(num[2]):
    print('yes')
else:
    print('no')
    
''' A Company insures its drivers in the following cases.
1. If the driver is married.
2. If the driver is unmarried, male and above 30 years of age.
3. if the driver is unmarried, female and above 25 years of age.
In all other cases, the driver is not insured. If the marital status, sex, age of the
driver are the inputs, write a program to determine whether the driver is insured
or not.'''

marital_status = input('enter married or unmarried :')
sex = input('enter male or female:')
age = int(input('enter age in number :'))

if marital_status == 'married':
    print('you are eligible for insurance')
else:
    if sex == 'male' and age > 30:
        print('you are eligible for insurance')
    elif sex == 'female' and age > 25:
        print('you are eligible for insurance')
    else:
        print('you are not eligible for insurance')

''' Write a program to read a character and find out whether it is uppercase or lowercase.'''

letter = input('enter letter:')

if letter.islower() == True:
    print('it is lowercase')
else:
    print('it is uppercase')


''' Write a program to print the uppercase letter of a given lowercase.'''

letter = input('enter letter:')

if letter.islower() == True:
    print(letter.upper())
else:
    print(letter.lower())


''' Write a program to check whether the given input is digit or lowercase character or uppercase character or a special
character.'''

data =input('enter same data :')

if data.isdigit() == True:
    print('it is in number')
elif data.islower() == True:
    print('it is in lower case')
elif data.isupper() == True:
    print('it is in upper case')
elif data in '!@#$%^&*':
    print('data is special characters')
else:
    print('input is invalid')


'''Write a program to check whether the given alphabet is a vowel or consonant'''
letter = input('enter any one alphabet :')

if letter.isalpha() == True:
    if letter in 'aeiouAEIOU':
        print(f'{letter} is vowel')
    else:
        print(f'{letter} is not vowel')
else:
    print('please enter only alphabets')


'''Write a program to numbers divisible by 7 and multiple of 5, between 1 and 100.'''

for i in range (1,101):
    if i%5==0 and i%7==0:
        print(i,end =',')
'''Write a program to find the oldest and youngest among 3 people.'''
person1 = int(input('enter person1 age in number:'))
person2 = int(input('enter person2 age in number:'))
person3 = int(input('enter person3 age in number:'))

if person1 > person2 and person1 >person3:
    print('person1')
elif person2 > person1 and person2 >person3:
    print('person2')
elif person3 > person2 and person3 >person1:
    print('person3')
   
        

