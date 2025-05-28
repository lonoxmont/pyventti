from card import Card
import random

class Deck:
    def __init__(self) -> None:
        self.deck = []
        self.suits = ("Hearts", "Diamonds", "Clubs", "Spades")
        self.face = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}

        # makes deck as soon as obj is made
        self._make_deck()
    
    def _make_deck(self):
        self.deck = [Card(suit, self.face[f]) if f in self.face else [Card(suit, f)]for suit in self.suits for f in range(1,14)]

    def shuffle(self):
        return random.shuffle(self.deck)

    # for when you want to print deck
    def __repr__(self):
        return self.deck
    
    def deal_card(self):
        return self.deck.pop