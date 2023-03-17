'''Write a class called Rock_paper_scissors that implements the logic of the game Rockpaper-scissors. For this game the user plays against the computer for a certain number of rounds. Your class should have fields for the how many rounds there will be, the current round number, andthenumberofwinseachplayerhas. There should bemethodsforgetting the computer’s choice, finding the winner of a round, and checking to see if someone has one the (entire) game. You may want more methods.'''
import random
class Rock_paper_scissors:
    def __init__(self,n,rand):   # n is number of rounds
        self.n=n
        self.rand= rand
        self.comp=random.choice(self.rand) #computer's choice'
    
    def comp_choice(self):
        return self.comp
       
    def winner_round(self,round):   #winner of one particular round
        self.round= round
        for i in range(1):
            self.user= input('pick your choice: ')
            if self.user=='rock' and self.comp== 'paper':
                return f'I picked {self.comp} I won this round'
            elif self.user== 'paper' and self.comp== 'rock':
                return f'I picked {self.comp}, You won this round'
            elif sslf.user== 'rock' and self.comp== 'scissors':
                return f'I picked {self.comp}, You won this round'
            elif self.user=='paper' and self.comp == 'scissors':
                return 'I picked {self.comp} I won thiz round'
            elif self.user== 'scissors' and self.comp== 'paper':
                return 'I picked {self.comp} You won this round'
            else:
                return 'There is a tie'
        
    def winner(self,score,c):   #Winner of the game
       self.score=score
       self.c=c
      
       if self.score>self.c:
           return  f'You won {self.score} rounds, YOU WON'
       elif self.scord<self.c:
           return f'I won {self.c} rounds, I WON'
       return 'We won equal rounds'
                
n= int(input('enter number of rounds: '))
rand=['rock','paper','scissors']
e= Rock_paper_scissors(n,rand)
score=0
c=0
for i in range(n): # the game process
            user= input('pick your choice: ')
            comp=random.choice(rand)
            if user=='rock' and comp== 'paper':
                print(f'I picked {comp} I won this round')
                c+=1
            elif user== 'paper' and comp== 'rock':
                print(f'I picked {comp}, You won this round')
                score+=1
            elif user== 'rock' and comp== 'scissors':
                print(f'I picked {comp}, You won this round')
                score+=1
            elif user=='paper' and comp == 'scissors':
                print(f'I picked {comp} I won this round')
                c+=1
            elif user== 'scissors' and comp== 'paper':
                print('I picked {comp} You won this round')
                score+=1
            elif user=='scissors' and comp == 'rock':
                print(f'I picked {comp} I won this round')
            else:
                print(f'I picked {comp}, There is a tie')
                
print(e.winner(score,c))


'''Write a class that inherits from the Card_group class of this chapter. The class should represent a deck of cards that contains only hearts and spaces, with only the cards 2 through 10 in each suit. Add a method to the class called next2 that returns the top two cards from the deck.'''
import random
class Card_group:
    def __init__(self,cards=[]):
        self.cards=cards
        
    def nextCard(self):
       return self.cards.pop(0)
       
    def hasCard(self):
       return len(self.cards)>0
      
    def size(self):
        return len(self.cards)
    def shuffle(self):
        random.shuffle(self.cards)
        
class Rep(Card_group):
    def __init__(self):
        self.cards=[]
        v= ['hearts','spades']
        for v in v:
            for i in range(2,11):
                self.cards.append([i,v])
                
                
    def next2(self):
        self.p= self.cards.pop(0)
        self.q= self.cards.pop(1)
        return f'top two cards are {self.p} and {self.q}'
        
deck= Rep()
print(deck.next2())
