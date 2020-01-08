class Card:
    def __init__(self, suit, value):
        self.suit_of_card = suit
        self.val_of_card = value

        if(value==1):
            self.name = "Ace"
        elif(value==11):
            self.name="Jack"
        elif(value==12):
            self.name="Queen"
        elif(value==13):
            self.name="King"
        else:
            self.name = str(value)

    def show(self):
        print(f"{self.name} of {self.suit_of_card}")


class Deck:
    def __init__(self):
        self.deck_of_cards = []

        suits = {"Hearts", "Clubs", "Diamonds", "Spades"}

        for suit in suits:
            for i in range(1, 14):
                new_card = Card(suit, i)
                self.deck_of_cards.append(new_card)

    def show_deck(self):
        for card in self.deck_of_cards:
            card.show()
        
first_deck = Deck()

first_deck.show_deck()