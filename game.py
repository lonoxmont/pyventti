from hand import Hand
from deck import Deck

def main(self, deck):
    self.deck = deck
    PlayerHand = Hand
    DealerHand = Hand
    Deck.shuffle()

    PlayerHand.draw_card()
    PlayerHand.draw_card()
    DealerHand.draw_card()

    print(f"your hand is {PlayerHand.__repr__}")
    print("would you like to (h)it or (s)tand?")
    choice = input()
    if len(choice) != 1 or choice.lower() != 'h' and choice.lower() != 's' :
        print("Perkele! Pick an option from the list!")
    
    if choice == "h":
        PlayerHand.draw_card()
        
            
    if choice == "s":
        pass




main(Deck)