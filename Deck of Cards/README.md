# Deck of Cards

The code was written using the Raspberry Pi python tutorial linked here --> (https://projects.raspberrypi.org/en/projects/deck-of-cards/0)

My goal is to explore object oriented programming and to explore a problem that I've been puzzling over for years. I haven't done much research on it because I'm using it as a thought experiment and test of my own skills, but I'm curious about how many perfect shuffles it would take to get a brand new deck of cards back into the exact order it was at the start.

Things to define:

  A Perfect Shuffle: Splitting a deck exactly in half and using a Riffle Shuffle where exactly one card from each half-deck goes down at a time, in order --> (L1,R1,L2,R2,L3,R3)
  
  Starting Order: All suits grouped together in this order --> (Hearts, Clubs, Diamonds, Spades). Hearts and Clubs are ordered (Ace through King). Diamonds and Spades are ordered (King through Ace).

  Top Deck: Hearts and Clubs

  Bottom Deck: Diamonds and Spades
  
  
  #Cardless Approach
  
  This approach was inspired by Bill Chapman while discussing a coding approach to this problem. Simply put, why deal with cards and objects when all I really need is just a list from 1-52?

