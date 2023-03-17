''' An acronym is an abbreviation that uses the first letter of each word in a phrase. We see them everywhere. For instance, NCAA for National Collegiate Athletic Association or NBC for National Broadcasting Company. Write a program where the user enters an acronym and the program randomly selects words from a wordlist such that the words would fit the acronym.'''

acr= input('enter acronymn: ').lower()
k=[line.strip() for line in open('/storage/emulated/0/py/corncob_lowercase.txt') ]
l=[]
count=0
for i in acr:
    for j in k:
            if i==j[0]:
                print(j,end= ' ' )
                break



#bbbbbbbbb

'''Write a program to cheat at the game Scrabble. The user enters a string. Your program should return a list of all the words that can be created from those seven letters'''
import random
player=input('enter a string: ')
k=[line.strip() for line in open('/storage/emulated/0/py/corncob_lowercase.txt')]
l=[]
for i in player:
    for j in k:
        for c in j[0]:
            if i== c:
               l.append(j)
                   
                    
print(l)
