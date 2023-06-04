Deck=[]
topDeck=[]
bottomDeck=[]
shuffledDeck=[]
newShuffledDeck=[]
newTopDeck=[]
newBottomDeck=[]
finalShuffledDeck=[]

for i in range(1,53):
    Deck.append(i)


def splitDeck():
    for i in range(len(Deck)):
        if i<26:
            topDeck.append(Deck[i])
        else:
            bottomDeck.append(Deck[i])


def shuffleDeck():
    if len(shuffledDeck)==0:
        for i in range(len(topDeck)):
            shuffledDeck.append(topDeck[i])
            shuffledDeck.append(bottomDeck[i])

        print("Shuffled Deck: ",shuffledDeck)

    if len(shuffledDeck)>0:
        for i in range(len(shuffledDeck)):
            if i<26:
                newTopDeck.append(shuffledDeck[i])
            else:
                newBottomDeck.append(shuffledDeck[i])

        print("New Top Deck: ",newTopDeck)
        print("New Bottom Deck: ",newBottomDeck)
        newShuffledDeck=newTopDeck+newBottomDeck
        
        #for i in range(len(topDeck)):
        #   newShuffledDeck.append(newTopDeck[i])
        #   newShuffledDeck.append(newBottomDeck[i])
    

    #for i in range((len(Deck)//2):len(Deck):1):
        #bottomDeck.append(Deck[i])

print("Starting Deck: ",Deck)
splitDeck()
print("...Splitting Deck...")
print("Top Deck: ",topDeck)
print("Bottom Deck: ",bottomDeck)

print("...Shuffling Deck...")
shuffleDeck()

#print("Shuffled Deck: ",shuffledDeck)

#print("New Top Deck: ",newTopDeck)
#print("New Bottom Deck: ",newBottomDeck)

#print("...Shuffling Deck Again...")
#shuffleDeck()
#print("New Shuffled Deck: ",newShuffledDeck)