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
        self._shuffledDeck=[]
        self.shuffle()
        print(self._shuffledDeck)

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
        for i in range(len(self._topDeck)):
            self._shuffledDeck.append(self._topDeck[i])
            self._shuffledDeck.append(self._bottomDeck[i])

        # # Cards[]
        # self._topDeck=[Card(s,n) for s in tSuits for n in tNumbers]
        # # Cards[]
        # self._bottomDeck=[Card(s,n) for s in bSuits for n in bNumbers]
        # # i = Card j = Card
        # for i 26 
        #  for j 26
        # 
        #
        # for i in _topDeck.length
        #   _shuffledDeck.append(_topDeck[i])
        #   _shuffledDeck.append(_bottomDeck[i])
        # 
        #         
        # self._shuffledDeck=[Card(i,j) for i in self._topDeck for j in self._bottomDeck]




        
        
my_shuffled_deck=Deck()
print(my_shuffled_deck)