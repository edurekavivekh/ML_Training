
1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included). Go to the editor
Click me to see the sample solution

def check_div_mul():
    y = []
    for i in range(1500,2700):
        if i%7 == 0 and i%5 == 0:
            y.append(i)
    return y

print("List of numbers those are divisible by 7 and multiple of 5, between 1500 and 2700 => {0}".format(check_div_mul()))


2. Write a Python program to convert temperatures to and from celsius, fahrenheit. Go to the editor
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ] 
Expected Output : 
60蚓 is 140 in Fahrenheit
45蚌 is 7 in Celsius 
Click me to see the sample solution

f = 45
#c/5 = f-32/9
c = ((f-32) * 5) / 9
print("{0} degree Fahrenheit is {1} degree celsius".format(f,int(c)))

#c/5 = f-32/9
#(c * 9) / 5 = f - 32
c = 60
f = ((c * 9) / 5 ) + 32

print("{0} degree celsius is {1} degree Fahrenheit".format(c,int(f)))


3. Write a Python program to guess a number between 1 to 9. Go to the editor
Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.
Click me to see the sample solution

import random
success = True
while success:
    i = int(input("Please enter the number to guess between 1 to 9 :"))
    number = random.randint(1,9)

    if (i >= 1) and (i <= 9) and (i == number):
        print("Congratulations!!!")
        success = False
    else:
        print("Actual Number was : {0}, Try it again".format(number))
        success = True




4. Write a Python program to construct the following pattern, using a nested for loop.

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
Click me to see the sample solution

5. Write a Python program that accepts a word from the user and reverse it. Go to the editor
Click me to see the sample solution

mystring = input("Enter the word :")
print("Reverse of word {0} is {1}".format(mystring, mystring[::-1]))

#alternate =>
for i in range(len(mystring)):
    print(mystring[i-1],end="")

6. Write a Python program to count the number of even and odd numbers from a series of numbers. Go to the editor
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
Expected Output : 
Number of even numbers : 5
Number of odd numbers : 4
Click me to see the sample solution
---------
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

even = 0
odd = 0
for i in range(len(numbers)):
    if (numbers[i] % 2) == 0 :
        even = even + 1
    else:
        odd = odd + 1

print("Number of even numbers :{0}".format(even))
print("Number of odd numbers :{0}".format(odd))

---------
7. Write a Python program that prints each item and its corresponding type from the following list.
Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
Click me to see the sample solution

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

for i in range(len(datalist)):
    print("{0} is of type: {1}".format(datalist[i], type(datalist[i])))

8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
Note : Use 'continue' statement. 
Expected Output : 0 1 2 4 5 
Click me to see the sample solution

for i in range(0,6):
    if i == 3 or i == 6:
        continue
    else:
        print(i, end=" ")

9. Write a Python program to get the Fibonacci series between 0 to 50. Go to the editor
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, .... 
Every next number is found by adding up the two numbers before it.
Expected Output : 1 1 2 3 5 8 13 21 34
Click me to see the sample solution
-------
fib = 0
for i in range(0,50):
    fib = fib + i
    print(fib)








10. Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
Sample Output : 
fizzbuzz
1
2
fizz
4 
buzz
Click me to see the sample solution


for i in range(50):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
        continue
    elif i % 3 == 0:
        print("fizz")
        continue
    elif i % 5 == 0:
        print("buzz")
        continue


11. Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j. Go to the editor
Note :
i = 0,1.., m-1 
j = 0,1, n-1.

Test Data : Rows = 3, Columns = 4 
Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
Click me to see the sample solution

row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col]= row*col

print(multi_list)

12. Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case). Go to the editor
Click me to see the sample solution


while True:
    line = input("Input :")
    print("Output :{0}".format(line.lower()))
    if line == "" :
        break



13. Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and print the numbers that are divisible by 5 in a comma separated sequence. Go to the editor
Sample Data : 0100,0011,1010,1001,1100,1001
Expected Output : 1010
Click me to see the sample solution

a = input("Input")
my_list = a.split(',')

for i in my_list:
    if (int(i, 2))%5 == 0 :
        print(i)


14. Write a Python program that accepts a string and calculate the number of digits and letters. Go to the editor
Sample Data : Python 3.2
Expected Output :
Letters 6 
Digits 2

a = 0
d = 0
data = [ x for x in input() ]
for i in data:
    if i.isalpha():
        a = a + 1
    elif i.isdigit():
        d = d + 1

print("Letters :{0}".format(a))
print("Digits :{0}".format(d))



Click me to see the sample solution

15. Write a Python program to check the validity of password input by users. Go to the editor
Validation :

At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.
Click me to see the sample solution

password = [ x for x in input() ]
a = 0
u = 0
d = 0
p = 0
for c in password:
    if c.isalpha():
        a = a + 1
        if c.isupper():
            u = u + 1
    elif c.isdigit():
        d = d + 1
    else:
        p = p + 1

if a > 0 and u > 0 and d > 0 and p > 0 and ( len(password) >= 6 or len(password) <= 16):
    print("Password is valid")
else:
    print("Password is invalid")

'''
import re
p= input("Input your password")
x = True
while x:  
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")

'''

16. Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence. Go to the editor
Click me to see the sample solution

for n in range(100,400):
    p = [int(x) for x in str(n)]
    if p[0]%2 == 0 and p[1]%2 == 0 and p[2]%2 == 0:
        print(n)



17. Write a Python program to print alphabet pattern 'A'. Go to the editor
Expected Output:

  ***                                                                   
 *   *                                                                  
 *   *                                                                  
 *****                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *
Click me to see the sample solution

from internet =>

result_str="";
for row in range(0,7):
    for column in range(0,7):
        if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):
            result_str=result_str+"*"
        else:
            result_str=result_str+" "
    result_str=result_str+"\n"
print(result_str);


18. Write a Python program to print alphabet pattern 'D'. Go to the editor
Expected Output:

 ****                                                                   
 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
 **** 
Click me to see the sample solution

19. Write a Python program to print alphabet pattern 'E'. Go to the editor
Expected Output:

 *****                                                                  
 *                                                                      
 *                                                                      
 ****                                                                   
 *                                                                      
 *                                                                      
 *****
Click me to see the sample solution

20. Write a Python program to print alphabet pattern 'G'. Go to the editor
Expected Output:

  ***                                                                   
 *   *                                                                  
 *                                                                      
 * ***                                                                  
 *   *                                                                  
 *   *                                                                  
  *** 
Click me to see the sample solution

21. Write a Python program to print alphabet pattern 'L'. Go to the editor
Expected Output:

 *                                                                      
 *                                                                      
 *                                                                      
 *                                                                      
 *                                                                      
 *                                                                      
 *****
Click me to see the sample solution

22. Write a Python program to print alphabet pattern 'M'. Go to the editor
Expected Output:

  *       *                                                             
  *       *                                                             
  * *   * *                                                             
  *   *   *                                                             
  *       *                                                             
  *       *                                                             
  *       *
Click me to see the sample solution

23. Write a Python program to print alphabet pattern 'O'. Go to the editor
Expected Output:

  ***                                                                   
 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
  *** 
Click me to see the sample solution

24. Write a Python program to print alphabet pattern 'P'. Go to the editor
Expected Output:

 ****                                                                   
 *   *                                                                  
 *   *                                                                  
 ****                                                                   
 *                                                                      
 *                                                                      
 *  
Click me to see the sample solution

25. Write a Python program to print alphabet pattern 'R'. Go to the editor
Expected Output:

 ****                                                                   
 *   *                                                                  
 *   *                                                                  
 ****                                                                   
 * *                                                                    
 *  *                                                                   
 *   *
Click me to see the sample solution

26. Write a Python program to print the following patterns. Go to the editor
Expected Output:

  ****                                                                  
 *                                                                      
 *                                                                      
  ***                                                                   
     *                                                                  
     *                                                                  
 **** 
 
 ooooooooooooooooo                                                       
ooooooooooooooooo                                                       
ooooooooooooooooo                                                       
oooo                                                                    
oooo                                                                    
oooo                                                                    
ooooooooooooooooo                                                       
ooooooooooooooooo                                                       
ooooooooooooooooo                                                       
             oooo                                                       
             oooo                                                       
             oooo                                                       
ooooooooooooooooo                                                       
ooooooooooooooooo                                                       
ooooooooooooooooo 
Click me to see the sample solution

27. Write a Python program to print alphabet pattern 'T'. Go to the editor
Expected Output:
 *****                                                                  
   *                                                                    
   *                                                                    
   *                                                                    
   *                                                                    
   *                                                                    
   *  
Click me to see the sample solution

28. Write a Python program to print alphabet pattern 'U'. Go to the editor
Expected Output:

 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
  *** 
Click me to see the sample solution

29. Write a Python program to print alphabet pattern 'X'. Go to the editor
Expected Output:

 *   *                                                                  
 *   *                                                                  
  * *                                                                   
   *                                                                    
  * *                                                                   
 *   *                                                                  
 *   *
Click me to see the sample solution

30. Write a Python program to print alphabet pattern 'Z'. Go to the editor
Expected Output:

*******                                                                 
     *                                                                  
    *                                                                   
   *                                                                    
  *                                                                     
 *                                                                      
*******
Click me to see the sample solution

31. Write a Python program to calculate a dog's age in dog's years. Go to the editor
Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
Expected Output:

Input a dog's age in human years: 15                                    
The dog's age in dog's years is 73
Click me to see the sample solution

32. Write a Python program to check whether an alphabet is a vowel or consonant. Go to the editor
Expected Output:

Input a letter of the alphabet: k                                       
k is a consonant.
Click me to see the sample solution

33. Write a Python program to convert month name to a number of days. Go to the editor
Expected Output:

List of months: January, February, March, April, May, June, July, August
, September, October, November, December                                
Input the name of Month: February                                       
No. of days: 28/29 days 
Click me to see the sample solution

34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20. Go to the editor

Click me to see the sample solution

35. Write a Python program to check a string represent an integer or not. Go to the editor
Expected Output:

Input a string: Python                                                  
The string is not an integer.  
Click me to see the sample solution

36. Write a Python program to check a triangle is equilateral, isosceles or scalene. Go to the editor
Note :
An equilateral triangle is a triangle in which all three sides are equal.
A scalene triangle is a triangle that has three unequal sides.
An isosceles triangle is a triangle with (at least) two equal sides.
Expected Output:

Input lengths of the triangle sides:                                    
x: 6                                                                    
y: 8                                                                    
z: 12                                                                   
Scalene triangle  
Click me to see the sample solution

37. Write a Python program that reads two integers representing a month and day and prints the season for that month and day. Go to the editor
Expected Output:

Input the month (e.g. January, February etc.): july                     
Input the day: 31                                                       
Season is autumn  
Click me to see the sample solution

38. Write a Python program to display astrological sign for given date of birth. Go to the editor
Expected Output:

Input birthday: 15                                                      
Input month of birth (e.g. march, july etc): may                        
Your Astrological sign is : Taurus 
Click me to see the sample solution

39. Write a Python program to display the sign of the Chinese Zodiac for given year in which you were born. Go to the editor
Expected Output:

Input your birth year: 1973                                             
Your Zodiac sign : Ox  
Click me to see the sample solution

40. Write a Python program to find the median of three values. Go to the editor
Expected Output:

Input first number: 15                                                  
Input second number: 26                                                 
Input third number: 29                                                  
The median is 26.0   
Click me to see the sample solution

41. Write a Python program to get next day of a given date. Go to the editor
Expected Output:

Input a year: 2016                                                      
Input a month [1-12]: 08                                                
Input a day [1-31]: 23                                                  
The next date is [yyyy-mm-dd] 2016-8-24   
Click me to see the sample solution

42. Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish. Go to the editor

Click me to see the sample solution

43. Write a Python program to create the multiplication table (from 1 to 10) of a number. Go to the editor
Expected Output:

Input a number: 6                                                       
6 x 1 = 6                                                               
6 x 2 = 12                                                              
6 x 3 = 18                                                              
6 x 4 = 24                                                              
6 x 5 = 30                                                              
6 x 6 = 36                                                              
6 x 7 = 42                                                              
6 x 8 = 48                                                              
6 x 9 = 54                                                              
6 x 10 = 60 
Click me to see the sample solution

44. Write a Python program to construct the following pattern, using a nested loop number. Go to the editor
Expected Output:

1
22
333
4444
55555
666666
7777777
88888888
999999999
Click me to see the sample solution