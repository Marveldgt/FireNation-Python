'''Chapter 4
Write a program that lets the user play Rock-Paper-Scissors against the computer. There should be five rounds, and after those five rounds, your program should print out who won and lost or that there is a tie'''
import random
import time
print('There are five rounds in this game, Are you ready to play rock paper scissors with me?\n')
count=0
time.sleep(1)
for i in range(5):    
    com=['rock', 'paper', 'scissors']
    user= input('pick your choice \n')
    comp= random.choice(com)
    compu=str(comp)
    if user==compu:
        count +=1
        print('correct')
    else:
        print('wrong')

print(f'You got {count} correctly, I got {5-count} correctly')
if count> (5-count):
    print('You Won')
elif count==(5-count):
    print('There\'s a tie')
else:
    print('I won')
    
''' Chapter 4       hhhhh              
Write a program that asks the user for an hour between 1 and 12, asks them to enter am or pm, and asks them how many hours into the future they want to go. Print out what the hour will be that many hours into the future, printing am or pm as appropriate. An example is shown below'''
print('enter hour between 1 and 12: ')
hour=int(input(' '))
print('am(1) or pm(2)')
tim= int(input(' '))
print('How many hours ahead?')
hour_add= int(input(' '))
new_hour= hour+hour_add
if tim==1:
    if new_hour>12 :
        print(f'new hour: {new_hour%12} pm ')
    elif new_hour<12:
        print(f'new hour: {new_hour} am ')
    elif new_hour==12:
        print(f'new hour: {new_hour} pm ')
elif tim==2:
    if new_hour>12 :
        print(f'new hour: {new_hour%12} am ')
    elif new_hour<12:
        print(f'new hour: {new_hour} pm ')
    elif new_hour==12:
        print(f'new hour: {new_hour} am ')   
