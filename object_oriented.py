'''Use the Standard_deck class of this section to create a simplified version of the game War. In this game, there are two players. Each starts with half of a deck. The players each deal the top card from their decks and whoever has the higher card wins the other player’s cards and adds them to the bottom of his deck. If there is a tie, the two cards are eliminated from play (this differs from the actual game, but is simpler to program). The game ends when one player runs out of cards.'''

class Standard_deck:
    def __init__(self): 
        self.cards=[] 
        for s in['Hearts','Diamonds','Clubs','Spades']: 
            for v in range(2,15):
                self.cards.append([v,s])   #append number,suit
    def game(self):
        import random
        random.shuffle(self.cards) #shuffle then divide the cards into two for player p and q
        self.p= self.cards[:26]   
        self.q= self.cards[26:]
        self.c=0
        while  self.c+1>0:
            if len(self.p) ==0 or len(self.q)==0:  # if one player card finishes
                        break
            else:  #checking for plsyer with card of higher number
                        if self.p[0][0] > self.q[0][0]: 
                            self.p.append(self.q[0])
                            del self.q[0]
                            print(f'player 1, you won this round, you have {len(self.p)} cards now')
                            self.c+=1
                        elif self.p[0][0]< self.q[0][0]:
                            self.q.append(self.p[0])
                            del self.p[0]
                            print(f'player 2, you won this round, you have {len(self.q)} cards now')
                            self.c+=1
                
                        else:
                             del self.p[0]
                             del self.q[0]
                             print(f'there was a tie')
                             self.c+=1
                 
    def winner(self):
            if len(self.p)> len(self.q):
                return f'winner is player 1'
            return f'winner is player 2'
       
e= Standard_deck()
print(e.game())
print()
print(e.winner())
