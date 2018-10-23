from hand import Hand

class Player:

    def __init__(self, name, chips = 100):
        self.name = name
        self.chips = chips
        self.hand = Hand()
        self.bet = 0

    def add_card(self, card):
        self.hand.add_card(card)
    
    def place_bet(self):
        while True:
            try:
                bet = int(input('You can bet up to {} chips, how much will you bet {}? '.format(self.chips, self.name)))
            except:
                print('Input a number please')
                continue
            else:
                if self.chips < bet and bet > 0:
                    continue
                break
        self.chips -= bet
        self.bet = bet

    def __str__(self):
        return '{}; Chips: {}; Bet: {}; Cards: {}'.format(self.name, self.chips, self.bet, self.hand)