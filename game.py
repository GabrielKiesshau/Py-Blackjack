from deck import Deck
from hand import Hand
from player import Player

def promptPlayer():
    while True:
        print('Your {}'.format(player.hand))

        action = input('Do you HIT or STAY {}? '.format(player.name)).upper()
        
        if action == 'HIT':
            player.hand.add_card(deck.deal())
            continue
        elif action == 'STAY':
            print('Player stays')
            break

print('Welcome to blackjack!')

name = input('What is your name, player? ')
player = Player(name)

while True:
    player.hand = Hand()

    deck = Deck()
    deck.shuffle()

    player.place_bet()
    player.hand.add_card(deck.deal())
    player.hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal(False))

    print(player)
    print('Dealer {}'.format(dealer_hand))

    playing = True

    while playing:

        promptPlayer()
        
        print(player)
        print('Dealer {}'.format(dealer_hand))

        if player.hand.isAbove21():
            print('You busted {}'.format(player.name))
            break
        else:
            while player.hand.sum > dealer_hand.sum:
                dealer_hand.add_card(deck.deal())

            print(player)
            print('Dealer {}'.format(dealer_hand))

            if dealer_hand.isAbove21():
                print('The dealer busted!')
                player.chips += (player.bet * 2)
                break
            elif dealer_hand.sum > player.hand.sum:
                print('Dealer wins')
                break
            else:
                print('Tie')
                break
    
    if player.chips > 0:
        print('You have {} chips {}'.format(player.chips, player.name))

        option = input('Play again? ').upper()

        if option in ['YES', 'Y']:
            continue
        else:
            print('Thanks for playing!')
            break
    else:
        print('You lost everything... Game Over')
        break