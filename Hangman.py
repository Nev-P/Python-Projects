import random
import sys
# Step One - Introudction / Draw the Gallow Artwork
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
# displays the starting gallows and name of game
def introduction():
    print("========== HANGMAN ==========")
    print(HANGMANPICS[0])

# empty the lists when we restart the game
def clearAlLlists():
    hiddenWordList.clear()
    originalWordList.clear()
    correctLettersGuessed.clear()
    incorrectLettersGuessed.clear()

introduction()

'''
* declaring al lists to be used in the game
* wordbank holds all words to randomly choose from 
* orgiginalworldlist is sed to check if guessed the correct word
* correctletterguessed holds all letters contained in the hiddenWordlist
incorrectLettersGuessed holds all the
'''

# Step Two - Decide on the Word to Use
wordBank = ["puppy", "thief", "clocks", "system", "pineapple"]
# Step Three - Draw the underlines for the word
hiddenWordList = []
originalWordList = []
correctLettersGuessed = []
incorrectLettersGuessed = []

# Game variables
gameOver = False
mistakes = 0

# Game loop
while not gameOver:
    # clear all lists to ensure a new game runs correctly
    clearAlLlists()
    mistakes = 0

    # A random word is chosen for the current loop
    hiddenWord = random.choice(wordBank)

# Creating the list for replacing underscores with letters
for i in range(len(hiddenWord)):
    hiddenWordList.append("_")

# Creating a correct list to compare the original word
for letter in hiddenWord:
    originalWordList.append(letter)

    # Printing out underscores for the player to start guessing
    print(hiddenWordList)
    while hiddenWordList != originalWordList and not mistakes == 6:
        # Step Four - Ask the user to guess a letter
        # User needs to enter input
        # We need to check if the length == 1
        # We need to check that it is not a number

        # Step Five - Check to see if correct or incorrect
        #      Step Five A
        #       If Right: Give Feedback
        #       Place letter at it's correct position and display it
        #       Add it to a list of correct guesses

        #      Step Five B
        #       If Wrong: Give Feedback
        #       Draw a body part on the gallow
        #       Add it to a list of incorrect guesses

        # Step Six - Repeat Until: Word has been guessed, or full body has been displayed

        foundLetter = False
        userAnswer = input("Please enter a letter >>")
        while len(userAnswer) != 1 or userAnswer.isnumeric():
            userAnswer = input("Please enter a valid letter >>")

        # Turn any letter input into a lowercase
        userAnswer = userAnswer.lower()


        # Pos in the number of the letter in the word
        # userAnswer is the guess we have made
        for pos in range(len(hiddenWord)):
            if hiddenWord[pos] == userAnswer:
                hiddenWordList[pos] = userAnswer
                foundLetter = True

        if not foundLetter:
            print("You have guessed an incorrect letter")
            mistakes += 1
            incorrectLettersGuessed.append(userAnswer)
        else:
            correctLettersGuessed.append(userAnswer)


        print(hiddenWordList)
        print("Correct Guesses")
        print(correctLettersGuessed)
        print("Incorrect Guesses")
        print(incorrectLettersGuessed)
        print(HANGMANPICS[mistakes])

    userChoice = input("Do you want to play again? (y/n)")
        if userChoice == "y" or userChoice == "n":
            print("Ok, let's play again")
        else:
            print("Ok, goodbye")
            sys.exit()
