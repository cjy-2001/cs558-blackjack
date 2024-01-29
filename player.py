from typing import Type
import random

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}
THRESHOLD_WIN_RATE = 0.4

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print(f'Invalid card: {suit} {rank}')

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def get_value(self):
        return VALUES[self.rank]


# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        ans = "Hand contains "
        for i in range(len(self.cards)):
            ans += str(self.cards[i]) + " "
        return ans
        # return a string representation of a hand

    def add_card(self, card):
        self.cards.append(card)
        # add a card object to a hand

    def get_value(self):
        value = 0
        aces = False
        for c in self.cards:
            rank = c.get_rank()
            v = VALUES[rank]
            if rank == 'A': aces = True
            value += v
        if aces and value < 12: value += 10
        return value
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video


# define deck class
class Deck:
    def __init__(self):
        self.deck = []
        for s in SUITS:
            for r in RANKS:
                self.deck.append(Card(s, r))
        # create a Deck object

    def shuffle(self):
        random.shuffle(self.deck)
        # shuffle the deck

    def deal_card(self):
        return self.deck.pop()
        # deal a card object from the deck

    def __str__(self):
        ans = "The deck: "
        for c in self.deck:
            ans += str(c) + " "
        return ans
        # return a string representing the deck
    

# define player class
class Player:

    def __init__(self):
        self.matrix = [[{'wins': 0, 'counts': 0} for _ in range(11)] for _ in range(22)]

    def should_hit(self, player_value: int, dealer_face_value: int) -> bool:
        if player_value >= 21:
            return False
        
        if player_value <= 11:
            return True 
        
        # Check if there's enough data in the matrix to make a decision
        if self.matrix[player_value][dealer_face_value]['counts'] > 200:
            win_rate = self.matrix[player_value][dealer_face_value]['wins'] / self.matrix[player_value][dealer_face_value]['counts']
            return win_rate >= THRESHOLD_WIN_RATE
        else:
            # Default strategy if not enough data
            return player_value < 17
        
    def dealer_turn(self, deck, dealer_hand):
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())

    def compare_hands(self, player_hand, dealer_hand):
        player_value = player_hand.get_value()
        dealer_value = dealer_hand.get_value()

        if player_value > 21:  # Player busts
            return False
        if dealer_value > 21:  # Dealer busts
            return True
        return player_value > dealer_value 
    
    def sim(self, trials: int) -> None:
        # Run random trials and update the matrix
        for _ in range(trials):
            deck = Deck()
            deck.shuffle()
            player_hand = Hand()
            dealer_hand = Hand()

            # Deal two cards to player and one to dealer
            player_hand.add_card(deck.deal_card())
            player_hand.add_card(deck.deal_card())
            dealer_hand.add_card(deck.deal_card())

            player_value = player_hand.get_value()
            dealer_face_value = VALUES[dealer_hand.cards[0].get_rank()]

            # Update the matrix
            result = self.matrix[player_value][dealer_face_value]
            result['counts'] += 1

            # Deal another card to player
            if player_value == 21:
                continue

            player_hand.add_card(deck.deal_card())
            player_value = player_hand.get_value()

            if player_value > 21:
                continue
            else:
                outer_break = False
                while self.should_hit(player_value, dealer_face_value):
                    player_hand.add_card(deck.deal_card())
                    player_value = player_hand.get_value()
                    if player_value > 21:
                        outer_break = True
                        break
                
                if outer_break:
                    continue 

            # Dealer's turn
            self.dealer_turn(deck, dealer_hand)

            if self.compare_hands(player_hand, dealer_hand):
                result['wins'] += 1

    def hitme(self, playerhand: Type[Hand], dealerfacecard: Type[Card]) -> bool:
        # use the matrix to decide whether to hit
        player_value = playerhand.get_value()
        dealer_face_value = VALUES[dealerfacecard.get_rank()]

        if player_value > 21:
            return False
        
        if player_value <= 11:
            return True
        
        win_rate = self.matrix[player_value][dealer_face_value]['wins'] / self.matrix[player_value][dealer_face_value]['counts']
        
        return win_rate >= THRESHOLD_WIN_RATE
        

    def play(self, trials: int) -> float:
        # play out trials with the learned matrix 
        wins = 0
        for _ in range(trials):
            deck = Deck()
            deck.shuffle()
            player_hand = Hand()
            dealer_hand = Hand()

             # Deal two cards to player and one to dealer
            player_hand.add_card(deck.deal_card())
            player_hand.add_card(deck.deal_card())
            dealer_hand.add_card(deck.deal_card())

            while self.hitme(player_hand, dealer_hand.cards[0]):
                player_hand.add_card(deck.deal_card())

            if player_hand.get_value() <= 21: 
                self.dealer_turn(deck, dealer_hand)

                if self.compare_hands(player_hand, dealer_hand):
                    wins += 1

        win_rate = wins / trials
        return win_rate

    def print_matrix(self):
            # Print column headers (dealer face values)
            print("", end="\t")
            for dealer_value in range(1, 11):
                print(dealer_value, end="\t")
            print()  # Newline after headers

            # Print each row with row header (player value)
            for player_value in range(4, 22):
                print(player_value, end="\t")  # Row header
                for dealer_value in range(1, 11):
                    cell = self.matrix[player_value][dealer_value]
                    if cell['counts'] > 0:
                        win_rate = (cell['wins'] / cell['counts']) * 100
                        print(f"{win_rate:.2f}%", end="\t")
                    else:
                        print("N/A\t", end="")
                print()


def main():
    player = Player()
    
    num_trials = 1000000
    player.sim(num_trials)
    player.print_matrix()
    print(player.play(10000))

if __name__ == '__main__':
    main()