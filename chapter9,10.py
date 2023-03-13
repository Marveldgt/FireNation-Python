'''Chapter 9
Write a program to play the following simple game.The player starts with $100.On each turn a coin is flipped and the player has to guess heads or tails.The player wins $9 for each  correct guess and loses $10 for each incorrect guess.The game ends either when the player runs out of money or gets to $200'''
import random
print('Welcome player, You Have $100\n ')
start= 100
while start>0:
    pick= input('Head(H) or Tail(T): ').lower()
    out= ['h','t']
    rand= random.choice(out)
    if pick==rand:
        start+=9
        print(f'Right,You have ${start} now \n')
        if start>= 200:
            print(f'You got a total ${start}, Congrats\n')
            break
        else:
            start   
    else:
        start-=10
        print(f'Wrong, You have ${start} left\n')
        if start<= 0:
            print('Game over, you lost all the $100')
            
     
'''Chapter 10    
Write a program that finds all integer solutions to Pell’s equation x2 −2y2 = 1, where x and y are between 1 and 100'''

for x in range(1,101):
    for y in range(1,101):
        if (x**2)-(2*(y**2))==1:
            print(x,',',y)
            
            
'''Write a program that asks the user for a number and prints out all the ways to write the number as difference of two perfect squares, x2 − y2, where x and y are both between 1 and 1000. Writing a number as a difference of two squares leads to clever techniques for factoring large numbers'''

num=int(input('enter a number: '))
for a in range(1,1000):
    for b in range(1,1000):
        if (a**2)-(b**2)==num:
            print(f'{a}^2 - {b}^2')
            
            

'''Pascal’s triangle is shown below. On the outside are 1’s and each other number is the sum of the two numbers directly above it. Write a program to generate Pascal’s triangle. Allow the user to specify the number of rows. Be sure that it is nicely formatted, like below'''


def fact(n):
         k=1
         if n==1 or n==0:
             return k
         else:
             return n*fact(n-1)

num = int(input('enter number of rows: '))
for i in range(0,num+1):
    k= fact(i)
    for j in range(num-i+1):
        print(end=' ')
    for j in range(0,i+1):
            l=i-j
            a= fact(l)
            b=fact(j)
            g=k//(a*b)
            print(g,end=' ')
            
    print()
