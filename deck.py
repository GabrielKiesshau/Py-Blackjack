import random
from card import Card

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = {'Ace': 11, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}

class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
        self.shuffle()
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self, facing_up = True):
        card = self.deck.pop()
        
        if facing_up == True:
            card.flip()
        
        return card

    def __str__(self):
        cards = ''

        for card in self.deck:
            cards += str(card)

        return cards
