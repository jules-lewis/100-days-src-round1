#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Both turn their paired cards face
# down, and add a further face down, then turn one face up. The player with the 
# higher cards takes both piles (six cards). If the turned-up cards are again 
# the same rank, each player places another card face down and turns another 
# card face up. The player with the higher card takes all 10 cards, and so on.
#
# If a player runs out of cards during WAR, they have lost.
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITS = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    cards = []
    def __init__(self):
        #create a basic deck
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append([rank, suit])

    def shuffle(self):
        #shuffles the deck using Random
        shuffle(self.cards)

    def split(self):
        #returns the deck in two halves
        return [self.cards[0:26], self.cards[26:]]

class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, hand = []):
        #create a hand, based on the list passed in
        self.cards = hand

    def __len__(self):
        return len(self.cards)

    def addCards(self, cards_to_add):
        self.cards.extend(cards_to_add)

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Player can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        #create a player with a Hand of cards
        self.name = name
        self.hand = hand

    def dealCard(self):
        return(self.hand.cards.pop(0))

    def canDeal(self):
        return (len(self.hand) > 0)


######################
#### GAME PLAY #######
######################
print("------------------------------------------------")
print("Welcome to War, let's begin...")
print("------------------------------------------------")
new_deck = Deck()
new_deck.shuffle()
hand_a = Hand(new_deck.split()[0])
hand_b = Hand(new_deck.split()[1])
player_1 = Player("Player 1", hand_a)
player_2 = Player("Player 2", hand_b)
discards = []

def cardAdmin(winningPlayer, losingPlayer, cardsToMove):
    print(winningPlayer.name + " wins this round...")
    winningPlayer.hand.addCards(cardsToMove)
    print("{} has {} cards, {} has {}.".format(winningPlayer.name, len(winningPlayer.hand), losingPlayer.name, len(losingPlayer.hand)))
    print("------------------------------------------------")        
    cont = input("Press Enter to continue....")


while (player_1.canDeal) and (player_2.canDeal):
    card_1 = player_1.dealCard()
    card_2 = player_2.dealCard()
    discards.append(card_1)
    discards.append(card_2)
    rank_1 = RANKS.index(card_1[0])
    rank_2 = RANKS.index(card_2[0])
    print(player_1.name + " plays " + str(card_1))
    print(player_2.name + " plays " + str(card_2))
    if rank_1 > rank_2:
        cardAdmin(player_1, player_2, discards)
        discards = []
    elif rank_2 > rank_1:
        cardAdmin(player_2, player_1, discards)
        discards = []
    else:
        print("War! Both players turn a card face down and carry on.")
        if (player_1.canDeal) and (player_2.canDeal):
            discards.append(player_1.dealCard())
            discards.append(player_2.dealCard())

if player_1.canDeal:
    print(player_1.name + " wins. " + player_2.name + " has no cards left.")
else:
    print(player_2.name + " wins. " + player_1.name + " has no cards left.")

