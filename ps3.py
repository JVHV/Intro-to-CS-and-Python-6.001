# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 5

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10,'*':0
}
# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
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

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    #1) Define: What is the word?
    
    #2) Define: SUM OF POINTS FOR LETTERS IN THE WORD. Use ?dictionary?, SCRABBLE_LETTER_VALUES for this.
    
    #3) Define: 7*wordlen - 3*(n-wordlen), where wordlen is the length of the word and n is the hand length when the word was played

    #4) Product of the two components

    """1) """
    first_component=0
    """2)"""
    for i in str.lower(word) :
        first_component= first_component + SCRABBLE_LETTER_VALUES[i] 
    """3)"""
    second_component= 7 * len(word) - 3 * (n-len(word))
    if second_component < 1:
        second_component=1
        
    """4")"""
    score= first_component * second_component
    
    return score

    
    
#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print (letter, end=' ')      # print all on the same line
    return ("")                               # print an empty line


#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    
    #1) I need to deal a * instead of a vowel
       #First option  # I can delete one vowel once that is dealt
       #Second option # I can deal one less vowel and deal a * 
    
    
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels-1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1 # I think the .get(x,0) +1 means that  if  key x has no value it gets the value 0, and then adds + 1 to that value
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1 
    x='*'
    hand[x]= hand.get(x,1) 
    
    return hand


# Problem #2: Update a hand by removing letters
#

def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    new_hand=hand.copy() 
    for i in str.lower(word):
        if i in new_hand:
            new_hand[i]-= 1
            if new_hand[i]<=0:
                del new_hand[i] 
    return new_hand 
#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    #1) Check if word is in word_list
    #2) Check if word is composed of letters in the hand
    #3) Return true if this conditions are alright, if not return False.
    #4) You can get an error if the letter is in the hand but you cannot use it no more. The letters has to be deleted or 
    #5) I need to make * indistinguible of a vowel
        #1) Create something that says that * is equal to any vowel
        #2) 
        
#Modify the is_valid_word function to support wildcards. Hint: 
#Check to see what possible words can be formed by replacing the wildcard with other vowels. 
#You may want to review the documentation for string module’s find() function and make note of itsbehavior 
#when a character is not found. The constant VOWELS defined for you at the top ofthe file may be helpful as well.

    """1) and 2) """ 
    valid_word=str.lower(word)
    hand_for_test=hand.copy() 
    
    for i in valid_word:
        if i not in hand_for_test: 
            return False
        
    if "*" in valid_word:
        find=word.find("*")
        s = list(word)
        for i in VOWELS:
            s[find] = i
            new_valid_word= ''.join(s)
            
            if new_valid_word in word_list:
                for i in word:
                    hand_for_test[i]-= 1
                    if hand_for_test[i]<=0:
                        del hand_for_test[i]   
                print (hand_for_test) 
                return True 
                
                
    
    if valid_word in word_list:
        for i in valid_word:
            if i not in hand_for_test: 
                return False 
            else:
                hand_for_test[i]-= 1
                if hand_for_test[i]<=0:
                   del hand_for_test[i]           
            
        return True 
    else: 
        return False      
    
# Problem #5: Playing a hand
#

def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    # I copied the method on display_hand function, I have to think in another method to do this.
    hand_length=0
    for letter in hand.keys():
         for j in range(hand[letter]): 
             hand_length= hand_length + 1
    
    return hand_length
    
    pass  # TO DO... Remove this line when you implement this function



def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    n= calculate_handlen(hand)
    total_score=0
    #1
    while n != 0: 
        #2
        print ("These are your letters:")
        print (display_hand(hand))
        #3
        word= input('Enter word, or "!!" to indicate that you are finished: ') 
        #4
        if word == "!!":
            #5
            print (total_score) 
            return "" 
        #6
        else:
            #7
            if is_valid_word(word, hand, word_list) == True:
                #8
                total_score= total_score + get_word_score(word,n) 
                print (word, "earned", get_word_score(word, n), "points. Tota5l:",total_score,"points")  # "Create total score"
                #9
            else:
                print ("Your word is not valid")
            #10    
            hand = update_hand(hand, word)
            n= calculate_handlen(hand)
            print (n) 
            
    
    print ('Ran out of letters. Total score:', total_score)           
    return "" 
    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score
    
#    1)# As long as there are still letters left in the hand:
#    
#       2) # Display the hand
#        
#       3) # Ask user for input
#        
#       4) # If the input is two exclamation points:
#        
#           5) # End the game (break out of the loop)
#
#            
#       6) # Otherwise (the input is not two exclamation points):
#
#           7) # If the word is valid:
#
#            8)  # Tell the user how many points the word earned,
#                # and the updated total score
#
#            9)# Otherwise (the word is not valid):
#                # Reject invalid word (print a message)
#                
#            10)# update the user's hand by removing the letters of their inputted word
#            
#
#  11) # Game is over (user entered '!!' or ran out of letters),
#    # so tell user the total score

    # Return the total score as result of function



#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    
    # ask the user if he wants to change a letter 
    # if he say no 
        #return
    # if he says yes
            # Substitute one of the letters and for a vowel or a consonant at random, does not mutate hand
            # return new hand copy
            
    new_hand= hand.copy()  
    ask= input(("Would you like to substitute a letter?")) 
    asklower= str.lower(ask) 
    
    if asklower == "no":
        return None
    elif asklower == "yes":
        letter= input ("Which letter would you like to replace?")
        for i in new_hand: 
            if i in letter:
                del new_hand[i]
                x = random.choice(VOWELS and CONSONANTS)
                new_hand[x]= new_hand.get(x, 1)
                return new_hand
            else:
                return hand 
                
                
        
    
       

def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    
    print("play_game not implemented.") # TO DO... Remove this line when you implement this function
    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
n=7 
hand= deal_hand(n) 

print (hand) 

print (substitute_hand(hand))










