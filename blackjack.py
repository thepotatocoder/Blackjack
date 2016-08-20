#python3

'''
    A Blackjack simulation

    5 rounds, one player, 100 beginning points
    aces are worth 1, face cards worth 10
    if a player busts, 21 is subtracted from their total score
'''
from random import shuffle
from collections import OrderedDict

__author__ = 'thepotatocoder'

#Deck dictionary
pydeck = OrderedDict()

pydeck = {
    "Ace of Hearts" : 1,
    "King of Hearts" : 10,
    "Queen of Hearts" : 10,
    "Jack of Hearts" : 10,
    "10 of Hearts" : 10,
    "9 of Hearts" : 9,
    "8 of Hearts" : 8,
    "7 of Hearts" : 7,
    "6 of Hearts" : 6,
    "5 of Hearts" : 5,
    "4 of Hearts" : 4,
    "3 of Hearts" : 3,
    "2 of Hearts" : 2,
    "Ace of Spades" : 1,
    "King of Spades" : 10,
    "Queen of Spades" : 10,
    "Jack of Spades" : 10,
    "10 of Spades" : 10,
    "9 of Spades" : 9,
    "8 of Spades" : 8,
    "7 of Spades" : 7,
    "6 of Spades" : 6,
    "5 of Spades" : 5,
    "4 of Spades" : 4,
    "3 of Spades" : 3,
    "2 of Spades" : 2,
    "Ace of Clubs" : 1,
    "King of Clubs" : 10,
    "Queen of Clubs" : 10,
    "Jack of Clubs" : 10,
    "10 of Clubs" : 10,
    "9 of Clubs" : 9,
    "8 of Clubs" : 8,
    "7 of Clubs" : 7,
    "6 of Clubs" : 6,
    "5 of Clubs" : 5,
    "4 of Clubs" : 4,
    "3 of Clubs" : 3,
    "2 of Clubs" : 2,
    "Ace of Diamonds" : 1,
    "King of Diamonds" : 10,
    "Queen of Diamonds" : 10,
    "Jack of Diamonds" : 10,
    "10 of Diamonds" : 10,
    "9 of Diamonds" : 9,
    "8 of Diamonds" : 8,
    "7 of Diamonds" : 7,
    "6 of Diamonds" : 6,
    "5 of Diamonds" : 5,
    "4 of Diamonds" : 4,
    "3 of Diamonds" : 3,
    "2 of Diamonds" : 2,
}

deck = []
hand = []
leave = 0;

class DeckBox():
    """docstring for a very smart deck box"""

    def __init__(self):
        ''' Inside every deck box there is a deck made from the pydeck dictionary'''
        #print(list(pydeck.items()))
        global deck
        deck = [(c,v) for c, v in pydeck.items()]
        #print(list(deck))

    def shuffledeck(self):
        ''' Shuffles the deck in a random way '''
        shuffle(deck)

    def printdeck(self):
        ''' Prints the deck onto the terminal '''
        print("--------------")
        for lul in deck:
            print(lul)
        print("--------------")

    def drawcard(self):
        global hand
        global deck

        hand.append(deck[0])
        del deck[0]

    def printhand(self):
        global hand

        print(hand)

box1 = DeckBox()
box1.shuffledeck()
while leave == 0:
    print("-------------------------------------------------")
    print("Select move: d - Draw | p - printhand |  q - quit")
    print(" ")
    opt = input(">>")
    print("-------------------------------------------------")

    if opt == "d":
        box1.drawcard()
    elif opt == "p":
        box1.printhand()
    elif opt == "q":
        leave = 1
