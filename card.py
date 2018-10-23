class Card:

    def __init__(self, suit, rank, hidden = True):
        self.suit = suit
        self.rank = rank
        self.hidden = hidden

    def flip(self):
        self.hidden = False
    
    def __str__(self):
        if self.hidden == True:
            return '?'
        return '{} of {}'.format(self.rank, self.suit) 