import random # Used to implement deck shuffling
from os import system # Used to clear display


# Setting Suit and Value Variables (Tuples)
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

#Accessing High score file
highscoretxt = open("highscore.txt", "r") #Opens highscore.txt to view and write
highscorenum = highscoretxt.readline().replace("\n", "")
highscorename = highscoretxt.readline()

highscoretxt.close() # Closes file

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
system('cls||clear')
print('Welcome to the Game')

# View rules
viewrules = input("Would you like to view the rules? (y/n): ")
if viewrules.lower() == "y":
    print("""
          Welcome to the Card Guessing Game!

The goal of the game is to guess whether the next card drawn from the deck will be higher or lower than the current card.

How to Play:
1. Starting the Game:  
   - The game begins with a shuffled deck of cards.
   - A card will be drawn and shown to you, along with its suit and rank (e.g., "5 of Hearts").

2. Making a Guess:
   - You need to decide whether the next card drawn from the deck will be higher or lower than the current card.
   - You will enter 'h' for "higher" or 'l' for "lower".

3. Card Rankings:
   - The cards are ranked from Ace (lowest) to King (highest)
   - Ace = 1, 2, 3, ..., 10, Jack = 11, Queen = 12, King = 13.

4. Scoring:
   - Correct Guess: You will earn 20 points if your guess is right.
   - Incorrect Guess: You will lose 15 points if your guess is wrong.
   - You will only be disquallified if you end the game with a negative score.

5. Game Rounds:
   - The game consists of 8 rounds (guesses). After each guess, the next card becomes the "current card," and you continue guessing until all 8 cards are played.

6. Ending the Game:
   - After 8 rounds, you’ll see your score, the highest score will be recorded.
   - You can choose to play again by pressing ENTER or quit the game by typing 'q'.

7. Initial Score:
   - You start the game with a score of 50 points.

Good luck, and have fun guessing whether the next card will be higher or lower!
          """)

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

    
    if score < 0: # User has negative score upon completion of round
        print(f'The minimum score to pass is 0, you got {score}. Your failed')

    else: # Users score is >= 0
        if score > int(highscorenum): # If player sets new high score

            print(f'your score was {score}, the previous high score of all time is {highscorenum} which was set by {highscorename}')
            name = input('Please type a username to be saved for the high score: ')

            highscoretxt = open("highscore.txt", "w") # Reopens file to write new highscore

            highscoretxt.write(str(score) + '\n' + name) # re-writes new highscore to file
            print("High score added")
            highscoretxt.close() # Closes file to save
        
        else:
            print(f'your score was {score}, the high score of all time is {highscorenum} which was set by {highscorename}') # Displays high score

    # Asks if player wants to play again
    goAgain = input('To play again, press ENTER, or "q" to quit: ')
    if goAgain == 'q': # Player wants to quit game
        break 

print('OK bye') # Exit message
