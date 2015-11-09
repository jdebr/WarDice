import random

_NUMDICE = 10



class Dice:
    def __init__(self, sides):
        self._sides = sides
        
    def roll(self):
        return random.randint(1, self._sides)
    
    
    
class Card:
    def __init__(self, suit, pips):
        self._suit = suit
        self._pips = pips
        
    def getSuit(self):
        return self._suit
    
    def getColor(self):
        if self._suit == 'Hearts' or self._suit == 'Diamonds':
            return 'Red'
        else:
            return 'Black'
    
    def getCard(self):
        if self._pips == 1:
            return 'Ace of ' + self._suit
        elif self._pips == 2:
            return 'Two of ' + self._suit
        elif self._pips == 3:
            return 'Three of ' + self._suit
        elif self._pips == 4:
            return 'Four of ' + self._suit
        elif self._pips == 5:
            return 'Five of ' + self._suit
        elif self._pips == 6:
            return 'Six of ' + self._suit
        elif self._pips == 7:
            return 'Seven of ' + self._suit
        elif self._pips == 8:
            return 'Eight of ' + self._suit
        elif self._pips == 9:
            return 'Nine of ' + self._suit
        elif self._pips == 10:
            return 'Ten of ' + self._suit
        elif self._pips == 11:
            return 'Jack of ' + self._suit
        elif self._pips == 12:
            return 'Queen of ' + self._suit
        elif self._pips == 13:
            return 'King of ' + self._suit
        else: return 'Bad Card!'
        
    def power(self):
        return self._pips
        
        
class Deck:
    def __init__(self):
        self.availableCards = []
        self.shuffle()
        
    def shuffle(self):
        for x in range(1,14):
            self.availableCards.append(Card('Hearts', x))
        for x in range(1,14):
            self.availableCards.append(Card('Spades', x))
        for x in range(1,14):
            self.availableCards.append(Card('Diamonds', x))
        for x in range(1,14):
            self.availableCards.append(Card('Clubs', x))
    
    def draw(self,):
        firstcard = random.randint(0, (len(self.availableCards)-1))
        drawnCard = self.availableCards[firstcard]
        del self.availableCards[firstcard]
        return drawnCard
    
    
if __name__ == "__main__":
    myDie = Dice(6)
    
    p1score = 0
    p2score = 0
    
    p1dice = _NUMDICE
    p2dice = _NUMDICE
    
    p1hand = []
    p2hand = []
    
    myDeck = Deck()
    
    for x in range(5):
        c = myDeck.draw()
        p1hand.append(c)
   
    for y in range(5):
        c = myDeck.draw()
        p2hand.append(c)
        
    print("Welcome to WAR DICE\n")
    p1name = input("Player 1, Enter Name: ")
    p2name = input("Player 2, Enter Name: ")
    
    for r in range(5):
        print("\nROUND" + str(r+1))
        #PLAYER 1
        print("\n", p1name)
        input("Hit ENTER when ready")
        print("Your cards are:")
        for i in range(len(p1hand)):
            print(str(i+1) + "." + p1hand[i].getCard())
            
        while True:
            try:
                p1choice = int(input("Which card will you play?"))
                if (p1choice > 0 and p1choice <= len(p1hand)): break
                else: print("Invalid selection.  Please try again.")
            except ValueError:
                print("Invalid selection.  Please try again.")
        
        print("\nYou have", p1dice,"dice left")
        
        while True:
            try:
                p1rolls = int(input("How many dice will you roll?"))
                if (p1rolls >= 0 and p1rolls <= p1dice): break
                else: print("Invalid selection.  Please try again.")
            except ValueError:
                print("Invalid selection.  Please try again.")
                
        print("You rolled")
        p1total = 0
        for d in range(p1rolls):
            myRoll = myDie.roll()
            print(myRoll)
            p1total += myRoll
        print("Total roll: " + str(p1total))        
        p1dice -= p1rolls
            
            
        #PLAYER 2
        print("\n", p2name)
        input("Hit ENTER when ready")
        print("Your cards are:")
        for i in range(len(p2hand)):
            print(str(i+1) + "." + p2hand[i].getCard())
            
        while True:
            try:
                p2choice = int(input("Which card will you play?"))
                if (p2choice > 0 and p2choice <= len(p2hand)): break
                else: print("Invalid selection.  Please try again.")
            except ValueError:
                print("Invalid selection.  Please try again.")
        
        print("\nYou have", p2dice,"dice left")
        
        while True:
            try:
                p2rolls = int(input("How many dice will you roll?"))
                if (p2rolls >= 0 and p2rolls <= p2dice): break
                else: print("Invalid selection.  Please try again.")
            except ValueError:
                print("Invalid selection.  Please try again.")
        
        print("You rolled")
        p2total = 0
        for d in range(p2rolls):
            myRoll = myDie.roll()
            print(myRoll)
            p2total += myRoll
        print("Total roll: " + str(p2total))
        p2dice -= p2rolls
        
        
        #RESOLUTION
        print("\n\n\n")
        input("Hit ENTER to battle!")
        p1power = (p1hand[(p1choice-1)].power() + p1total)
        p2power = (p2hand[(p2choice-1)].power() + p2total)
        del p1hand[(p1choice-1)]
        del p2hand[(p2choice-1)]
        print("\n" + p1name + " has " + str(p1power))
        print("\n" + p2name + " has " + str(p2power))
        print("\n\n\n")
        input("Hit ENTER for next round!")
        print("\n\n\n")