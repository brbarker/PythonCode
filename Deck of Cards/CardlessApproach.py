Deck=[]
topDeck=[]
bottomDeck=[]

for i in range(1,53):
    Deck.append(i)


def splitDeck():
    for i in range(len(Deck)//2):
        topDeck.append(Deck[i])



splitDeck()
print(Deck)
print(topDeck)