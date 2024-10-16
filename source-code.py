import random

# Setting Suit and Value Variables (Tuples)
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

# Sets number of cards for each game
NCARDS = 8

# Function to deal card by removing it from the deck
def getCard(deckListIn):
    thisCard = deckListIn.pop() # Removes top card and returns it
    return thisCard

# Function to Shuffle order of deck 
def shuffle(deckListIn):
    deckListOut = deckListIn.copy() # Create copy of deck
    random.shuffle(deckListOut) # Shuffles copy of deck
    return deckListOut # Returns shuffled deck

# Intro message
print('Welcome to the Game')
print('The programmer has forgotten to give you the game instructions.')

# Creates starting deck by combining suits and ranks
startingDeckList = []
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE): # Creates Values for each card
        cardDict = {'rank':rank, 'suit':suit, 'value':thisValue + 1} # Creates dictionary representing cards
        startingDeckList.append(cardDict) # Adds created card to Starting Deck

# Sets starting score
score = 50

# Main game loop, repeats until user quits
while True:
    print()
    gameDeckList = shuffle(startingDeckList) # Shuffles deck for game
    currentCardDict = getCard(gameDeckList)

    # Gets first card from shuffled deck
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']    
    print('Starting card is:', currentCardRank + ' of ' + currentCardSuit) #Displays starting card
    print()

    # Loop to play NCARDS amount of times (Default is 8)
    for cardNumber in range(0, NCARDS):   # play one game of this many cards
        answer = input('Will the next card be higher or lower than the ' + 
                               currentCardRank + ' of ' + 
                               currentCardSuit + '?  (enter h or l): ')
        answer = answer.casefold()  # Forces answer to be lowercase

        # Draws next card
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print('Next card is:', nextCardRank + ' of ' + nextCardSuit)

        # Checks players answer
        if answer == 'h': # Player guessed higher
            if nextCardValue > currentCardValue: # If next card was higher
                print('You got it right, it was higher')
                score = score + 20 # Increase score
            else:
                print('Sorry, it was not higher')
                score = score - 15 # Decrease score

        elif answer == 'l': # Player guessed lower
            if nextCardValue < currentCardValue: # If next card was lower
                score = score + 20 # Increase score
                print('You got it right, it was lower')
            else:
                score = score - 15 # If next card was higher
                print('Sorry, it was not lower')

        # Displays updated score
        print('Your score is:', score)
        print()

        # Updates current card to next card
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue
        currentCardSuit = nextCardSuit

    # Asks if player wants to play again
    goAgain = input('To play again, press ENTER, or "q" to quit: ')
    if goAgain == 'q': # Player wants to quit game
        break 

print('OK bye') # Exit message
