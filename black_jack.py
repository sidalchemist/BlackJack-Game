import random
playing=True

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
  

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'ACE':
            self.aces+=1
    
    def adjust_for_ace(self):
        while self.value >21 and self.aces:
            self.value-=10
            self.aces-=1
        

class Chips:
    
    def __init__(self,total=100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet?"))
        except:
            print("Sorry please provide an integer")
        else:
            if chips.bet > chips.total:
                print("Sorry you dont have enough chips! You have {}".format(chips.total))
            else:
                break


def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing

    while True:
        x=input("Hit or Stand?? Enter h or s: ")

        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("Player Stands Dealer's Turn")
            playing = False
        else:
            print("Sorry I did not understand that,Please Enter h or s only")
            continue

        break

def show_some(player,dealer):
    print("\n")
    print("DEALER HAND: ")
    print("one card hidden")
    print(dealer.cards[1])
    print("\n")
    print("PLAYERS HAND")
    for card in player.cards:
        print(card)

def show_all(player,dealer):
    print("\n")
    print("DEALERS HAND")
    for card in dealer.cards:
        print(card)
    print("\n")
    print("PLAYERS HAND")
    for card in player.cards:
        print(card)

def push(player, dealer):
    print("Dealer and Player tie!! PUSH")

def player_busts(player,dealer,chips):
    print("Player Bust")
    chips.lose_bet()
def player_win(player,dealer,chips):
    print("Player Won")
    chips.win_bet()

def dealer_bust(player,dealer,chips):
    print("Player WIN!! Dealer BUSTED!")
    chips.win_bet()

def dealer_win(player,dealer,chips):
    print("DEALER WINS!! Player BUst")
    chips.lose_bet()

while True:
    print("WELCOME - BLACKJACK")

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    print("\n")
    palyer_chips = Chips()

    take_bet(palyer_chips)

    show_some(player_hand,dealer_hand)

    while playing:
        hit_or_stand(deck,player_hand)
        
        show_some(player_hand,dealer_hand)

        if player_hand.value >21 :
            player_busts(player_hand,dealer_hand,palyer_chips)

            break
    if player_hand.value<21 :

        while dealer_hand.value < 17:
            hit(deck,dealer_hand)

        show_all(player_hand,dealer_hand)

        if dealer_hand.value > 21:
            dealer_bust(player_hand,dealer_hand,palyer_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_win(player_hand,dealer_hand,palyer_chips)
        elif dealer_hand.value < player_hand.value:
            player_win(player_hand,dealer_hand,palyer_chips)
        else:
            push(player_hand,dealer_hand)
        

    print("Players Total chips are at {}".format(palyer_chips.total))

    new_game = input("y/n")

    if new_game[0].lower() == 'y':
        playing=True
        continue
    else:
        print("Thankyou for playing!")
        break

