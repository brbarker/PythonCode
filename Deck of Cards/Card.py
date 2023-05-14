class Card:

    def __init__(self, suit, number):
        self._suit = suit
        self._number = number

    def __repr__(self):
        return self._number + " of " + self._suit

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, suit):
           if suit in ["hearts", "clubs", "diamonds", "spades"]:
               self._suit = suit
           else:
               print("That's not a suit!")

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        valid = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
        if number in valid:
            self._number = number
        else:
            print("That's not a valid number")


class Deck:

    def __init__(self):
        self._cards = []
        self._topDeck=[]
        self._bottomDeck=[]
        self.splitDeck()
        print("Top Deck =",self._topDeck)
        print("Bottom Deck =", self._bottomDeck)

    def populate(self):
        suits=["hearts","clubs","diamonds",'spades']
        numbers=[str(n) for n in range(2,11)]+["J","Q","K","A"]
        self._cards=[Card(s,n) for s in suits for n in numbers]

    def splitDeck(self):
        tSuits=["hearts","clubs"]
        tNumbers=["A"]+[str(n) for n in range(2,11)]+["J","Q","K"]
        bSuits=["diamonds","spades"]
        bNumbers=["K","Q","J","10","9","8","7","6","5","4","3","2","A"]
        self._topDeck=[Card(s,n) for s in tSuits for n in tNumbers]
        self._bottomDeck=[Card(s,n) for s in bSuits for n in bNumbers]

    def shuffle(self):
        self.splitDeck()
        
        
my_split_deck=Deck()
print(my_split_deck)