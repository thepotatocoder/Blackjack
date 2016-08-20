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

game_points = 100
game_round = 1
deck = []
hand = []
points= 0;
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
        global points

        hand.append(deck[0])
        del deck[0]
        card = hand[-1][0]
        value = hand[-1][1]
        points += int(value)

        print("You drew the ", end="")
        print(card, end="")
        print("! That's ", end="")
        print(value, end=" ")
        print("point", end="")
        if value > 1:
            print("s", end=" ")
        else:
            print(" ")
        print("more, making a total of ", end="")
        print(points, end=" ")
        print("point", end="")
        if points > 1:
            print("s", end="")
        print("!")

        if points >= 21:
            self.roundover()

    def printhand(self):
        global hand
        print(hand)

    def roundover(self):
        '''
        Initiates the round over procedure.
        '''
        global game_points
        global points
        global hand

        print("Round over! - Cause: ", end="")
        if points > 21:
            print("Too many points!")
        elif points == 21:
            print("BLACKJACK! PogChamp")
        else:
            print("Passed turn!")

        print("Points lost: ", end="")
        points_lose = points - 21
        game_points -= points_lose
        print(points_lose)
        print("Total points: ",end="")
        print(game_points)

                #New round
        hand = []
        points = 0

        dummy = input("Insert any string to continue to next round!")
        print("--------------------------------------------")
        self.startdeal()

    def passturn(self):
        self.roundover()

    def startdeal(self):
        print("New round! Dealing two cards...")
        self.drawcard()
        self.drawcard()



def userinput(opt, box):
    global leave
    if opt == "d":
        box.drawcard()
    elif opt == "p":
        box.passturn()
    elif opt == "q":
        leave = True

box1 = DeckBox()
box1.shuffledeck()
box1.startdeal()

while leave == False:
                #Get input from user
    print("----------------------------------------------")
    print("Select move: d - Draw | p - pass |  q - quit")
    print(" ")
    opt = input(">>")
    print("----------------------------------------------")
    userinput(opt, box1)

                #Check stuff
