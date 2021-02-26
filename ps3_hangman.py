# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    secretWordList = list(secretWord)
    distinctLetters = list()
    numberOfMatchingLetters = 0

    #First make a list of all the distinct letters and print them out
    for i in secretWordList:
        if i not in distinctLetters:
            distinctLetters.append(i)
    #print(distinctLetters)

    #For every distinct letter from the word, check if that letter is present in letters guessed. If all distinct letters are guessed, return True
    for i in distinctLetters:
        if i in lettersGuessed:
            numberOfMatchingLetters += 1
    if numberOfMatchingLetters == len(distinctLetters):
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    secretWordList = list(secretWord)
    distinctLetters = list()
    numberOfMatchingLetters = 0
    stringOfMatchingLetters = ''

    for i in secretWordList:
        if i in lettersGuessed:
            stringOfMatchingLetters += i
        else:
            stringOfMatchingLetters = stringOfMatchingLetters + '_ '
    return stringOfMatchingLetters



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    allLetters = 'abcdefghijklmnopqrstuvwxyz'
    allLetters = list(allLetters)
    missingLetters = list()
    stringOfMissingLetters = ''
    for i in allLetters:
        if i not in lettersGuessed:
            missingLetters.append(i)
    stringOfMissingLetters = ''.join(missingLetters)
    return stringOfMissingLetters


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    #secretWord = 'banana'
    secretWordList = list(secretWord)
    lettersGuessed = list()
    mistakesMade = 0
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is '+str(len(secretWord))+ ' letters long')
    numberOfGuesses = 8
    while 8 - mistakesMade > 0:
        if isWordGuessed(secretWord, lettersGuessed) == True:
          print('--------')
          print('Congratulations, you won!')
          break
        else:
            print('--------')
            print('You have '+str(8 - mistakesMade)+ ' guesses left.')
            #Calling getAvailableLetters() automatically deletes letters from lettersGuessed from the list of all available letters
            print('Available letters: '+str(getAvailableLetters(lettersGuessed)))
            userGuess = input('Please guess a letter: ')
            if userGuess in secretWord and userGuess not in lettersGuessed:
                lettersGuessed.append(userGuess)
                print('Good guess:'+getGuessedWord(secretWord,lettersGuessed))
            elif userGuess in lettersGuessed:
                print("Oops! You've already guessed that letter:"+getGuessedWord(secretWord,lettersGuessed))
            elif userGuess not in secretWord:
                print("Oops! That letter is not in my word: "+getGuessedWord(secretWord,lettersGuessed))
                lettersGuessed.append(userGuess)
                mistakesMade += 1
          
        if 8 - mistakesMade == 0:
          print('--------')
          print('Sorry you ran out of guesses. The word was ',secretWord)
          break
        else:
          continue
      






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
