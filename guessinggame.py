import random
print('Welcome! play this random guess game and have fun \n')
print('in the easy level, you guess a letter between a and e and a number between 0 and 5\n')
print('in the normal level, you guess a letter between a and k and a number between 0 and 20\n')
print("you have 100 points\n")
#instructions 
difficulty=input('enter difficulty level: easy or normal\n') #difficulty level
guess=str(input('which would you like to guess Letter(L) or Number(N)\n')).lower() #mode
score = 100
def repeat():  #defing function to loop the program
    global score
    
    
     # All players have a score of 100 at the start
    if guess=='n':     #if user chooses to guess a number
         num= input('guess a number\n')
         if difficulty=='easy':
            #if user picks easy guessing number
            en_num=random.randint(0,5) 
            #random number
            if en_num==num:
                #if user input equals random number increase score by 10
                score += 10
                print(f'correct,you got {score} point')
            else:
                    #if user input does not equal random number, reduce score by 1
                    score -=10
                    print('Try again, the answer is ',en_num,'you got',score,'points')
         else:
            #if  the user picks normal level
            num_2=random.randint(0,20)
            if num==num_2: #if user input is correct
                score += 10 #increase score by 10
                print(f'you got {score} point')
            else:
                #if user input is incorrect
                score -=10
                print('Try again,the answer is ',num_2,'you got',score,'points')
    else:
        #if user choose to guess a letter
        let= input('guess a letter\n') 
        if difficulty=='easy':
            #if user picks easy level
            vow= 'ae'
            #easy level
            en_let=random.choice(vow)
            if en_let==let:
                #if user is correct
                score +=10 #increase score by 10
                print(f'you got {score} point')
            else:
                #if user is not correct
                score -= 10 #reduce score by 10
                print('wrong, the answer is ',en_let,'you got',score,'points')
        else:
            #if user pick normal level
            const='abcdefghijk'
            let_2=random.choice(const)
            if en_let==let_2:
                    #if user got the random letter right
                    score += 10 #increase score by 10
                    print(f'you got {score} point')
            else:
                #if user is wrong
                score -=10
                print(f'Try again,the answer is {let_2}, you got a total of {score} points')
while True:
    repeat()
    cont= input('enter "y" to continue playing or any letter to quit\n')
    if cont=='y':
        continue
    print('bye') 
    quit()
