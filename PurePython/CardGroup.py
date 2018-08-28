from PlayingCards import *
import random as r

class Cards_Group:
    def __init__(self, cards = []):
        self.cards = cards

    def getCard(self):
        return self.cards.pop(0)

    def hasCard(self):
        return len(self.cards).__gt__(0)

    def size(self):
        return len(self.cards)

    def shuffle(self):
        r.shuffle(self.cards)
    

class Deck(Cards_Group):
    def __init__(self):
        self.cards = []
        self.cardList = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        for s in self.cardList:
            for v in range(2, 15):
                self.cards.append(Cards(v, s))

class PinochleDeck(Cards_Group):
    def __init__(self):
        self.cards = []
        self.cardList = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        for s in self.cardList*2:
            for v in range(9, 15):
                self.cards.append(Cards(v, s))


deck = Deck()
deck.shuffle()

newCard = deck.getCard()
print('\n', newCard)
choice = input('Higher (h) or Lower (l): ')
streak = 0

while choice.__eq__('h') or choice.__eq__('l'):
    if not deck.hasCard():
        deck = Deck()
        deck.shuffle()

    oldCard = newCard
    newCard = deck.getCard()

    if choice.lower.__eq__('h') and newCard.value.__gt__(oldCard.value) or \
    choice.lower.__eq__('l') and newCard.value.__lt__(oldCard.value):
        streak += 1
        print("Right! That's ", streak, " in a row!")

    elif choice.lower.__eq__('h') and newCard.value.__lt__(oldCard.value) or \
    choice.lower.__eq__('l') and newCard.value.__gt__(oldCard.value):
        streak = 0
        print("Completely wrong!")
    
    else:
        print("Push.")

    print('\n', newCard)
    choice = input('Higher (h) or Lower (l): ')

