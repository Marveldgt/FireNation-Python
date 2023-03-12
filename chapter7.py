'''Chapter 7
Write a program that asks the user for a message and encrypts the message using the one-time pad. First convert the string to lowercase. Any spaces and punctuation in the string should be left unchanged. For example, Secret!!! becomes thebmv!!! using the shifts above
(b) Write a program to decrypt a string encrypted as above'''

import random
message = input("Enter a message: ").lower()

alphabet = list('abcdefghijklmnopqrstuvwxyz')
secret = []
for character in message:
    if character in alphabet:
        i = random.randint(0,26)
        secret.append(alphabet[i])
    else:
        secret.append(character)

print(''.join(secret))

"""  b. Write a program to decrypt a string encrypted as above. """

message = list(message)
i = 0
secret_rev = []
for character in secret:
    secret_rev.append(message[i])
    i += 1
    
print(''.join(secret_rev))

'''Write a program that asks the user to enter a length. The program should ask them what unit the length is in and what unit they would like to convert it to. The possible units are inches, yards, miles, millimeters, centimeters, meters, and kilometers. While this can be done with 25 if statements, it is shorter and easier to add on to if you use a two-dimensional list of conversions, so please use lists for this problem'''
import time

u= int(input('enter a length: '))
print('follow the format inches(0), metre(1), yards(2), miles(3),millimeter(4), centimeter(5), kilometer(6)')
time.sleep(2)
r= int(input('enter unit: '))
p= int(input('enter unit you want to conver it to: '))
a,b,c,d,e,f,g= u, (u*0.0254), (u*0.028), (u*0.0000159), (u*25.4), (u*2.54), (u*0.0000254)
K=[[a,b,c,d,e,f,g] for k in range(7)]
K[1]= [u/0.0254,u,u/0.9144,u*0.00062,u*1000,u*100,u/1000]
K[2]= [u/0.028,u*0.9144,u,u*36000,u*914.4,u*91.44,u*0.0009144]
K[3]= [u/0.0000159,u/0.00062,u/36000,u,u/0.00000062,u/0.0000062]
K[4]= [u/25.4,u/1000,u/914.4,u*0.00000062,u,u/100,u/1000000]
K[5]= [u/2.54,u/100,u/91.44,u*0.0000062,u*10,u,u/100000]
K[6]= [u/0.0000254,u*1000,u/0.0009144,u*0.0000062,u*1000000,u*100000,u]
print(K[r][p])
