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
    d = {}  #create dictionary
    for i in secretWord: #runs through the secret word
      if i not in d:     #if the letter in secret word is not a key in the dictionary, create it
        d[i] = 1
      else:              #if letter in secret word is already a key, then add 1
        d[i] += 1
      
    for i in lettersGuessed: #for every letter in the lettersguessed
      if i in d:             #if the letter guessed is a part of the secret word, it will set the value to 0
        d[i] = 0
    
    val = d.values()
    for i in val:              
      if i > 0:              #if the value of the dictionary is greater than 0, the word is not guessed
        return False
    return True              #otherwise, the word is guessed.


      
    

# When you've completed your function isWordGuessed, uncomment these three lines
# and run this file to test!

secretWord = 'apple'
lettersGuessed = ['e', 'k', 'o', 'p', 'r', 's']
print(isWordGuessed(secretWord, lettersGuessed))

# Expected output:
# False


