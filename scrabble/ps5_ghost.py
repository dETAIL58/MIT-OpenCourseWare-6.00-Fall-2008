# Problem Set 5: Ghost
# Name: 
# Time: 2:00
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

#

def get_letter(player):
    """
    Returns an ascii single character.
    Ask's the specific player for the input.

    player: int
    return: string (UPPERCASE)
    """
    isLetter = False
    while isLetter == False:
        letter = raw_input("Player %d says letter: " % player)
        if letter in string.ascii_letters and letter not in string.whitespace:
            isLetter = True
    return string.upper(letter)


def possible_word(word):
    """
    Check's to see if there are any possible words can be
    formed given the input.

    word: string
    return: boolean
    """
    wordlist[:len(word)]
    for value in wordlist:
        if word.lower() == value[:len(word)]: return True
    return False

def valid_word(word):
    """
    Returns True/False response if word is a valid word
    and greater than three characters.

    word: string
    return: boolean
    """
    if word.lower() in wordlist and len(word) > 3: return True
    else: return False


def ghost():
    end = False
    word = ''
    
    print "Welcome to Ghost!"

    while end == False:
        for player in range (1,3):
            print "Current word fragment: '%s'" % (word)
            print "Player %d's turn." % (player)
            word += get_letter(player)
            print
            if possible_word(word):
                if valid_word(word):
                    print "Player %d looses because '%s' is a word!"\
                          % (player, word)
                    end = True
                    break
            else:
                print "Player %d looses because no word begins with '%s'!"\
                      % (player, word)
                end = True
                break
            

# Start the game
play = True

while play:
    ghost()
    print
    answer = raw_input("Do you want to play again? [Y/N]: ")
    if answer.upper() == 'N': play = False
