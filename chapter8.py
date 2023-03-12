'''Chapter 8
Write a program that creates a 10×10 list of random integers between 1 and 100. Then do the following: (a) Print the list. (b) Find the largest value in the third row. (c) Find the smallest value in the sixth column'''

from random import randint
L=[[randint(1,100) for r in range(10)] for c in range(10)]
from pprint import pprint
pprint(L)

print('\n',max(L[2]), end='\n\n ') #minimum value in row 3
    
col= [L[i][5] for i in range(len(L))]
print(min(col)) #minimum value in column 6


'''Chapter 8
Here is an old puzzle question you can solve with a computer program. There is only one f ive-digit number n that is such that every one of the following ten numbers shares exactly one digit in common in the same position as n. Find n'''

LST = ['01265','12171', '23257', '34548', '45970', '56236', '67324', '78084', '89872', '99414']
print(LST)
for i in range(10000,100000):
    all_ok = 'y'
    for c in range(len(LST)):
        cnt = 0
        for r in range(len(LST[0])):
            if LST[c][r:r+1] == str(i)[r:r+1]:
             cnt += 1
        if cnt != 1:
            all_ok = 'n'
            break
    if all_ok == 'y':
        print('number is', i)
