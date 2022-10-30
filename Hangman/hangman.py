# Hangman game
# Helper code

import random

WORDLIST_FILENAME = "words.txt"
pics = ['''
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
=========''','''
               
  +---+
  |   |
  O   |
 /|\  |
 / \_  |
      |
=========''','''
               
  +---+
  |   |
  O   |
 /|\  |
_/ \_ |
      |
=========''']

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

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    final = ''
    for char in secretWord:
        for letter in lettersGuessed:
          if letter == char:
            final+= letter
    return final==secretWord

def getGuessedWord(secretWord, lettersGuessed):
    product=[]
    for char in secretWord:
        if char in lettersGuessed:
            product.append(char)
        else:
            product.append('_')
        final = ''
    for let in product:
        final += let
    return final

def getAvailableLetters(lettersGuessed):
    alpha = 'abcdefgijklmnopqrstuvwxyz'
    result = ''
    for letter in alpha:
        if letter not in lettersGuessed:
            result+=letter
    return result
    
def hangman(secretWord):
    print('Welcome to Hangman!')
    print('I am thinking of a', len(secretWord), "letter word!")
    count = 8
    lettersGuessed = []
    while True:
        print('You have', count, 'guesses left.')
        print('Available letters:', getAvailableLetters(lettersGuessed))
        guess = input('Please guess a letter: ')
        if guess in secretWord and guess not in lettersGuessed:
            lettersGuessed.append(guess)
            print('Good Guess:', getGuessedWord(secretWord, lettersGuessed))
        elif guess in lettersGuessed:
            print('Oops! You have already guessed that letter:', getGuessedWord(secretWord, lettersGuessed))
        else:
            print('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
            lettersGuessed.append(guess)
            count-=1
            print(pics[-count-1])  
        print ("-----------------------------------")
        if count == 0:
            print('You LOSE. The word was:', secretWord)
            break
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('You Win!!! GOOD JOB!')
            break
    
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)




