from Player import Player
from Deck import Deck

choice = input("enter your name? ")
print('your answer was: ' + choice)
player1 = Player(choice)
dealer = Player('Dealer')

bob = Deck()
bob.build_deck()
bob.shuffle()

while input("Play a hand of blackjack?"):
    
    player1.hand.append(bob.deal_card())
    player1.hand.append(bob.deal_card())
    dealer.hand.append(bob.deal_card())
    dealer.hand.append(bob.deal_card())
    print()
    player1.print_hand(len(player1.hand))
    player1.get_hand_value()
    print()
    dealer.print_hand(1)
    dealer.get_hand_value()

    while player1.get_hand_value() < 21 :
        choice_hit =input("hit or say? type 'h' for hit or 'return' to stay")
        if choice_hit:
            player1.hand.append(bob.deal_card())
        else:
            break
        
        player1.print_hand(len(player1.hand))
        print(player1.get_hand_value())
        
        if player1.is_bust():
            print("you busted")
            break 

    

    if not player1.is_bust():
        while dealer.get_hand_value() < 17:
            dealer.hand.append(bob.deal_card())
            dealer.print_hand(len(dealer.hand))
            print(dealer.get_hand_value())
            if dealer.is_bust():
                print("dealer busted")



    if dealer.get_hand_value() > player1.get_hand_value() and not dealer.is_bust() or player1.is_bust():
        dealer.score += 1
        print("you lose")
        
    else:
        print("you win")
        player1.score += 1

    
    print(f"Player hand value: {player1.get_hand_value()} || Dealer hand value: {dealer.get_hand_value()}")
    print(f"Player Wins: {player1.score}")
    print(f"Dealer Wins: {dealer.score}")

    player1.hand = []
    dealer.hand = []







# bob.deal_card()
# print(len(bob.cards))
# bob.deal_card()
# print(len(bob.cards))