import random

from card import Card
from config import SUITS, RANKS

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