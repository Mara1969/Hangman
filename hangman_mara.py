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
wordlist = load_words()


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
    
    guessed = ""
    for letter in secret_word:
        if letter in letters_guessed:
            guessed += letter
        else: 
            guessed += "_ "
    return guessed 

       


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    lower_case_letters = string.ascii_lowercase # string comprised of lowercase letters
    available_letters = ""
    for letter in lower_case_letters:
        if letter not in letters_guessed:
            available_letters += letter  
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
    print('Welcome to the game Hangman!')
    length = len(secret_word)
    print(f'I am thinking of a word that is {length} letters long.')
    
    print('You have 3 warnings left.')
    print('------------')
    guesses = 6
    warnings = 3
    letters_guessed = []
    number_of_guesses = 0 
    vowels = 'aeiou'
    unique_letters = set(secret_word)
    length_unique_letters = len(unique_letters)

    while guesses > 0:
        letters_guessed_so_far = get_guessed_word(secret_word, letters_guessed)
        print(f'You have {guesses} guesses left.')
    
        print(f'Available letters: {get_available_letters(letters_guessed)}')
        user_input = input('Please guess a letter: ').lower()
        
        number_of_guesses += 1
        
        if not user_input.isalpha():
            if warnings > 0:
                warnings -= 1
                print(f'Oops! That is not a valid letter. You have {warnings} warning left: {letters_guessed_so_far}')
            elif warnings == 0:
                guesses -= 1
                print(f'Oops! That is not a valid letter. You have {warnings} warning left. So you lose one guess: {letters_guessed_so_far}')
            
            continue 
        
        if user_input in letters_guessed:
            if warnings == 0:
                guesses -= 1
                print(f'You already guessed that letter. You have {warnings} warnings left. So you lose one guess: {letters_guessed_so_far}')
            elif warnings > 0:
                warnings -= 1
                print(f'You already guessed that letter. You now have {warnings} warnings left: {letters_guessed_so_far}')
        
                continue 
        
        letters_guessed.append(user_input)
        
        if user_input in vowels and user_input not in secret_word:
            guesses -= 2
            print(f'Oops! That letter is not in my word: {letters_guessed_so_far}')
            
            continue 
        
        letters_guessed_so_far = get_guessed_word(secret_word, letters_guessed)
        
        
        
        if user_input in secret_word:
            print(f'Good guess: {letters_guessed_so_far}')
        else:
            print(f'Oops! That letter is not in my word: {letters_guessed_so_far}')
            guesses -= 1
            
            continue
            
        
        print('------------')
        
        if letters_guessed_so_far == secret_word:
           score = guesses * length_unique_letters
           print('Congatulations, you won!')
           print(f'Your total score for this game is: {score}')
           
           break 
            
    
    if letters_guessed_so_far != secret_word:
        print(f'Sorry, you ran out of guesses. The word was {secret_word}.')
        




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
    
    my_word = my_word.replace(" ", "")
    
    if len(my_word) != len(other_word):
        return False 
    
    for i in range(len(my_word)): 
        mw_char = my_word[i]
        ow_char = other_word[i]
        
        if mw_char != ow_char and mw_char != "_": 
            return False 
    return True
    



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
    
    my_word = my_word.replace(" ", "")
    matches = []
    
    for word in wordlist:
        if len(my_word) == len(word):
            match = True 
            
            for i in range(len(my_word)):
                    mw_char = my_word[i]  
                    ow_char = word[i]
                    
                    
                    if mw_char != "_" and mw_char != ow_char:
                        match = False
                        break  # No need to check further if there is a mismatch
                
                
            if match:
                matches.append(word)
            
    if matches:
        return " ".join(matches)
    else:
        return "No matches found"

                
             
    
   
        
        
      
            
            
            
    



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
    print('Welcome to the game Hangman!')
    length = len(secret_word)
    print(f'I am thinking of a word that is {length} letters long.')
    
    print('You have 3 warnings left.')
    print('------------')
    guesses = 6
    warnings = 3
    letters_guessed = []
    number_of_guesses = 0 
    vowels = 'aeiou'
    unique_letters = set(secret_word)
    length_unique_letters = len(unique_letters)

    while guesses > 0:
        letters_guessed_so_far = get_guessed_word(secret_word, letters_guessed)
        print(f'You have {guesses} guesses left.')
    
        print(f'Available letters: {get_available_letters(letters_guessed)}')
        user_input = input('Please guess a letter: ').lower()
        
        number_of_guesses += 1
        
        if user_input == '*':
            print(f'Possible word matches are: {show_possible_matches(letters_guessed_so_far)}')
            
            continue
        
        if not user_input.isalpha():
            if warnings > 0:
                warnings -= 1
                print(f'Oops! That is not a valid letter. You have {warnings} warning left: {letters_guessed_so_far}')
            elif warnings == 0:
                guesses -= 1
                print(f'Oops! That is not a valid letter. You have {warnings} warning left. So you lose one guess: {letters_guessed_so_far}')
            
            continue 
        
        if user_input in letters_guessed:
            if warnings == 0:
                guesses -= 1
                print(f'You already guessed that letter. You have {warnings} warnings left. So you lose one guess: {letters_guessed_so_far}')
            elif warnings > 0:
                warnings -= 1
                print(f'You already guessed that letter. You now have {warnings} warnings left: {letters_guessed_so_far}')
        
                continue 
        
        letters_guessed.append(user_input)
        
        if user_input in vowels and user_input not in secret_word:
            guesses -= 2
            print(f'Oops! That letter is not in my word: {letters_guessed_so_far}')
            
            continue 
        
        letters_guessed_so_far = get_guessed_word(secret_word, letters_guessed)
        
        
        
        if user_input in secret_word:
            print(f'Good guess: {letters_guessed_so_far}')
        else:
            print(f'Oops! That letter is not in my word: {letters_guessed_so_far}')
            guesses -= 1
            
            continue
            
        
        print('------------')
        
        if letters_guessed_so_far == secret_word:
           score = guesses * length_unique_letters
           print('Congatulations, you won!')
           print(f'Your total score for this game is: {score}')
           
           break 
            
    
    if letters_guessed_so_far != secret_word:
        print(f'Sorry, you ran out of guesses. The word was {secret_word}.')



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
