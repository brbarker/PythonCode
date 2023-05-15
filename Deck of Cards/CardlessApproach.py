Deck=[]
topDeck=[]
bottomDeck=[]

for i in range(1,53):
    Deck.append(i)


def splitDeck():
    for i in range(len(Deck)//2):
        topDeck.append(Deck[i])

    for i in Deck[26:53]:
        bottomDeck.append(i)

def shuffleDeck():
    for i in topDeck[26:1]:
        Deck.append(topDeck[i])
        Deck.append(bottomDeck[i])



    #for i in range((len(Deck)//2):len(Deck):1):
        #bottomDeck.append(Deck[i])

splitDeck()
shuffleDeck()

print(Deck)
print(topDeck)
print(bottomDeck)