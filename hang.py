import random
import string
import os

WORDLIST_FILENAME = "palavras.txt"

def loadWords():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):

    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False

    return True

def getGuessedWord():

     guessed = ''


     return guessed


def tryanotherletter(lettersGuessed, secretWord):
    _=os.system("clear")
    guessed = getGuessedWord()
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_'

    print 'Oops! You have already guessed that letter: ', guessed

def hangman(secretWord):
    guesses = len(loadWords())
    lettersGuessed = []
    while  isWordGuessed(secretWord, lettersGuessed) == False and guesses >0:

        available = string.ascii_lowercase
        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')

        print 'Available letters', available
        letter = raw_input('Please guess a letter: ')
        if letter in lettersGuessed:
            tryanotherletter(lettersGuessed, secretWord)

        elif letter in secretWord:
            lettersGuessed.append(letter)
            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '
            print 'Good Guess: ', guessed

        else:
            guesses -=1
            lettersGuessed.append(letter)

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Oops! That letter is not in my word: ',  guessed
        print '------------'

    else:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print 'Congratulations, you won!'
        else:
            _=os.system("clear")
            print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'



def menu():
    print 'Welcome to the game, Hangman!'
    print 'Menu'
    print ("       1 - New game\n       2 - Exit")
    option = raw_input ()
    if option=="1":
        _=os.system("clear")
        secretWord = loadWords().lower()
        hangman(secretWord)
    elif option=="2":
        _=os.system("clear")
        print 'YOU\nARE\nA\nLOSER\nDO\nIT\nAGAIN'
        menu(0)
    else:
        menu(0)
_=os.system("clear")
menu()
