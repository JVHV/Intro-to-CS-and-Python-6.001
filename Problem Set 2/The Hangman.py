# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

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
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

"""wordlist shut it down but run it on hangman"""
#wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
        
    return True 


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_word_guessed = (' ')  
    for letter in secret_word:
        if letter not in letters_guessed:
            secret_word_guessed = secret_word_guessed + ('_ ') 
        else:
            secret_word_guessed= secret_word_guessed + letter
    return secret_word_guessed 
        
            
        
    



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #string.ascii_lowercase imports all the lowercase english letters 
    #import string 
    available_letters = ' '   
    for i in string.ascii_lowercase:
        if i not in letters_guessed:
            available_letters = available_letters + i
    return available_letters


    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
#==============================================================================
 
#Steps to running Hangman:
#
#1) Load the available words in the list.
#
#2) Say Hi to the user and welcome him.
#
#3) Select a word to guess at random.
#
#4) Tell the user how many letter has the word.
#
#5) User start with 3 warnings. Tell the user how many warnings has.
#
#6) User Start with 6 guesses. Tell the user how many guesses he has. 
#
#7) Tell the user how many available letters has or the remaining ones.
#
#8) Ask the user to guess a letter. 
#
#9) Check If the user inputted an alphabet or if the input is an already used letter. Use str.isalpha(' ') 
#   9.1)  If he commited a fault. Tell the user how many warning has and that he can only input alphabet letters or that he already use that letter, then skip to 11). If he has none warnings left, he losses a guess.
#   9.2)  If it is an alphabet. Change every input to lowercase using str.lower (' ') 
#
#10) Tell the user wheter the guess is good or not.
#    If the guess is bad: 
#         10.1) If it is a consonant, user loses one guess. 
#         10.2) If its a vowel, user loses two guesses.
#
#11) Display the letters in the word that has been guessed, the letter that hasn't been guessed are displayed as "_"
#
#12) Print (-----) to help separate individual guesses from each other
#
#13) Evaluate if the game is over: 
#        13.1) If user has no guess left he loses and a message will print out (you lose...)  
#        13.2) If all the letters have been guessed in secret word the player wins and a message will print out telling his score (congratulations...)
#
#14) Start loop from 6) to 13) with the new values 


#=============================================================================='''
wordlist = load_words()
letters_guessed=''
vowels = 'aeiou'
guesses_remaining = 6
game_over= False
warnings_remaining = 3 
unique_letter=0

head='  l0'
torso='  |' 
foot= '/'
foot_two= '/ \ '
arm= ' /|'
arm_two= ' /|\ '

#2)    
print  ('Welcome to the game Hangman!')   
    
#3) 
secret_word = choose_word(wordlist) 
#print (secret_word)   
#4) 
print ('I am thinking of a word that is',len(secret_word),'letters long')
    
#5) 


print ('You have',warnings_remaining,'warnings left')
    

#6)     
while (game_over!=True) : 
    print ('--------------------------------')
    print ('You have',guesses_remaining,'guesses left')
     
    #7) 
    print ('Available letters:',get_available_letters(letters_guessed))      
               
    #8) 
    user_guess=str.lower( input('Please guess a letter:'))     
    
    #9), 10) and 11)        
    if user_guess in get_available_letters(letters_guessed): 
        letters_guessed= letters_guessed+user_guess
        if user_guess in secret_word:
            print('Good guess:',(get_guessed_word(secret_word, letters_guessed)))
            unique_letter= unique_letter + 1
        else:
            if user_guess in vowels:
                guesses_remaining = guesses_remaining - 2
            else:
                guesses_remaining = guesses_remaining - 1
            print ("Oops, that letter it's not in my word:",(get_guessed_word(secret_word, letters_guessed))) 
            
       
        
    elif str.isalpha(user_guess)== False: 
         warnings_remaining= warnings_remaining - 1      
         if warnings_remaining <=0 :
            guesses_remaining-= 1 
            print ("You have to introduce an alphabet letter. You have no warnings left so you lose one guess")
         else:
             print ("You have to introduce an alphabet letter, you have",warnings_remaining," warnings left :")
         
    else:
        warnings_remaining= warnings_remaining - 1
        if warnings_remaining <=0 :
            guesses_remaining-= 1 
            print ("Oops! You've already guessed that letter. You have no warnings left so you lose one guess")
        else:    
            print ("Oops! You've already guessed that letter. You have",warnings_remaining," warnings left :")
            
    print ('\n')    
    if guesses_remaining==5:
        print (foot) 
    
    if guesses_remaining==4:
        print ((torso),'\n',(foot))   
    
    if guesses_remaining==3:
        print (torso,'\n',foot_two)
    
    if guesses_remaining==2:
        print  (arm,'\n',foot_two)
        
    if guesses_remaining ==1:
        print (arm_two,'\n',foot_two)
    
    if guesses_remaining ==0:
        print (head,'\n',arm_two,'\n ',foot_two) 
    print ('\n')   
    
    #13    
    if is_word_guessed(secret_word, letters_guessed):
        print('Congratulations, you won!') 
        game_over=True 
    
    else:
        if guesses_remaining <= 0:
            print ('You lose sorry')
            game_over=True
            
score= guesses_remaining * unique_letter
print ('Your score was:',score)        
print ('The word is:',secret_word)    
    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
