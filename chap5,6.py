'''This exercise is about the well-known Monty Hall problem. In the problem, you are a contestant on a game show. The host, Monty Hall, shows you three doors. Behind one of those doors is a prize, and behind the other two doors are goats. You pick a door. Monty Hall, who knows behind which door the prize lies, then opens up one of the doors that doesn’t contain the prize. There are now two doors left, and Monty gives you the opportunity to change your choice. Should you keep the same door, change doors, or does it not matter?
  Write a program that simulates playing this game 10000 times and calculates what percentage of the time you would win if you switch and what percentage of the time you would win by not switching'''

import random
result= ['goat','prize']
percent=0
for i in range(1000):
    a=random.choice(result) #your choice    
    if str(a)=='prize':
        percent+=0.1
    else:
        percent
print(f'You would win {round(percent,2)} % if you didnt change your choice ')

'''Chapter 5
Write a program that asks the user to enter a number and prints the sum of the divisors of that number. The sum of the divisors of a number is an important function in number theory’'''
s=0
user= int(input('enter a number'))
for i in range(1,user+1):
    if user%i==0:
        s+=i
    else:
        s=s
print(f'sum of all divisor is {s}\n\n')

import random
L=[[random.randint(1,101)] for i in range(10) for j in range(10)]
print(L)


'''Chapter 6
In calculus, the derivative of x^4 is 4x^3. The derivative of x^5 is 5x^4. The derivative of x6 is 6x5. This pattern continues. Write a program that asks the user for input like x^3 or x^25 and prints the derivative. For example, if the user enters x^3, the program should print out 3x^2.'''

prob= input(' ')
pow= int(prob[2:])
d = str(pow-1)
answer= str(pow) + str(prob[:1])+'^'+d
print(f'derivative of {prob} is {answer}')
