from deck import ranks

class Hand:

    def __init__(self):
        self.cards = []
        self.sum = 0

    def add_card(self, card):
        self.cards.append(card)
        self.sum += ranks.get(card.rank)
    
    def isAbove21(self):
        print(self.sum)
        return self.sum > 21
    
    def __str__(self):
        cards = ''

        for card in self.cards:
            cards += '{} | '.format(card)

        return 'Cards: {}'.format(cards)