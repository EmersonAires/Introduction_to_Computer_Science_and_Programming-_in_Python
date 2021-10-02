# Problem Set 2, hangman.py
# Name: Emerson Eduardo Aires Nunes
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


def is_word_guessed(secret_word, list_letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    list_letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in list_letters_guessed;
      False otherwise
    '''
  
    number_letters_guessed = 0

    for secret_letter in secret_word:
        for letter__chosen in list_letters_guessed:
            if secret_letter == letter__chosen:
                number_letters_guessed += 1
                break
    
    if number_letters_guessed == len(secret_word):
        return True
    else:
        return False



def get_guessed_word(secret_word,
                     letter,
                     list_secret_word_dashes,
                     guesses,
                     remaining_letters):
    '''
    secret_word: string, the word the user is guessing
    list_letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
   
    user_guessed_letters = ""
    letter_position = 0
    some_guessed_letter = False

    for secret_letter in secret_word:
                      
        if secret_letter == letter:
            user_guessed_letters = user_guessed_letters + secret_letter
            list_secret_word_dashes[letter_position] = secret_letter
            some_guessed_letter = True
        else:
            user_guessed_letters = user_guessed_letters + "_ "

        letter_position += 1
    
    if some_guessed_letter:
        central_print('good_guess', secret_word, '', guesses,
                      remaining_letters, list_secret_word_dashes)
 
        return list_secret_word_dashes

    else:
        central_print('not_my_word', secret_word, '', guesses,
                      remaining_letters, list_secret_word_dashes)

        return list_secret_word_dashes
        


def get_available_letters(list_letters_guessed):
    '''
    list_letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = ""
    for letter_ascii in string.ascii_lowercase:
        count_letter = 0
        for letter in list_letters_guessed:
            if letter_ascii == letter:
                count_letter += 1
                break
        if count_letter == 0:
            available_letters = available_letters + letter_ascii
    
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
    ########################################################################################
    #variable assignment
    list_letters_guessed = []
    remaining_letters = string.ascii_lowercase
    guesses = 6
    end_of_the_game = False
    letter = ''
    list_secret_word_dashes = secret_word_dashes(secret_word)
    warnings_left = 3

    ########################################################################################
    #game presentation
    central_print('presentation', secret_word, warnings_left, guesses,
                  remaining_letters, list_secret_word_dashes)
    ########################################################################################
    
    while end_of_the_game != True:
        #user chooses a letter
        end_of_the_game, letter, guesses, warnings_left = letter_chosen_by_the_user(
                                                                                    end_of_the_game,
                                                                                    warnings_left,
                                                                                    guesses,
                                                                                    list_letters_guessed,
                                                                                    secret_word, remaining_letters, list_secret_word_dashes)
            
        if end_of_the_game:
            print("Sorry, you ran out of guesses. The word was {}"
                  .format(secret_word))
            break

        else:
            list_letters_guessed.append(letter)
            remaining_letters = get_available_letters(list_letters_guessed)

            #analyzes the letter chosen by the user
            list_secret_word_dashes = get_guessed_word(
                                                       secret_word, letter,
                                                       list_secret_word_dashes,
                                                       guesses,
                                                       remaining_letters)

        if is_word_guessed(secret_word, list_letters_guessed):
            print("Congratulations, you won!")
            print("You total score for this game is: {}".format(guesses*unique_letters(secret_word)))
            break



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
    
    list_position_letters = []
    ascii_lower_case = string.ascii_lowercase
    count = 0
    my_word = my_word.replace(' ', '')

    if len(my_word) != len(other_word):
        return False

    # storing the position of valid letters
    for letter_my_word in my_word:
        if letter_my_word in ascii_lower_case:
            list_position_letters.append(count)
        count += 1

    # checking the letter combination
    if len(list_position_letters) != 0:
        for i in list_position_letters:
            if my_word[i] != other_word[i]:
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

'''
if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)
'''

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)

#################################################################################################################
def letter_chosen_by_the_user(end_of_the_game,
                              warnings_left,
                              guesses,
                              list_letters_guessed,
                              secret_word,
                              remaining_letters,
                              list_secret_word_dashes):
    '''
    Returns the letters chosen by the user on each attempt
    '''
    valid_letter = False

    while not valid_letter and not end_of_the_game:
        letter_guessed = (input("Please guess a letter: "))
        valid_letter, end_of_the_game, guesses, warnings_left = game_rules(warnings_left,
                                                                           guesses,
                                                                           letter_guessed,
                                                                           list_letters_guessed,
                                                                           secret_word,
                                                                           remaining_letters, list_secret_word_dashes)
    
       # print("--------------------")

    return (end_of_the_game, letter_guessed, guesses, warnings_left)

################################################################################################################    

def secret_word_dashes(secret_word):
    '''
      returns a string hiding the secret_word with underlines
    '''
    list_secret_word_dashes = []
    i = 0
    while i < len(secret_word):
      list_secret_word_dashes.append('_ ')
      i += 1
    
    return list_secret_word_dashes

#################################################################################################################

def game_rules(warnings_left,
               guesses,
               letter_guessed,
               list_letters_guessed,
               secret_word,
               remaining_letters,
               list_secret_word_dashes):
    '''
    Rules of the game
    '''
    valid_letter = False
    # check the chosen letter
    if str.isalpha(letter_guessed) != True: # if the letter is not a valid character
        warnings_left, guesses = is_not_valid_letter(warnings_left, 
                                                     guesses,
                                                     remaining_letters,
                                                     list_secret_word_dashes)
    else:
         
        if letter_guessed in list_letters_guessed: # if the letter has already been chosen
            warnings_left, guesses = letter_has_already_been_chosen(warnings_left,
                                                                    guesses,
                                                                    remaining_letters, list_secret_word_dashes)

        else: # if the letter has not yet been chosen
            guesses = if_the_letter_has_not_yet_been_chosen(letter_guessed, guesses,
                                                            secret_word,
                                                            )
            valid_letter = True
    
    if guesses < 1: # end of the game
        return (valid_letter, True, guesses, warnings_left)
    else:
        return (valid_letter, False, guesses, warnings_left)


#################################################################################################################

def is_not_valid_letter(warnings_left,
                        guesses,
                        remaining_letters,
                        list_secret_word_dashes):
    '''
    Return invalid letter message and update warnings_left or guesses variable value
    '''

    if warnings_left >= 1:
        warnings_left -= 1

        central_print('not_valid_caracter_warnings_left', '', warnings_left, guesses,
                      remaining_letters, list_secret_word_dashes)
        
        return (warnings_left, guesses)
    else:
        guesses -= 1

        central_print('not_valid_caracter_guesses', '', warnings_left, guesses,
                      remaining_letters, list_secret_word_dashes)

        return (warnings_left, guesses)


#################################################################################################################
def letter_has_already_been_chosen(warnings_left,
                                   guesses,
                                   remaining_letters,
                                   list_secret_word_dashes):
    '''
    returns error message letter already chosen and updates warnings_left 
    or guesses variable.
    '''

    if warnings_left >= 1:
        warnings_left -= 1

        central_print('already_guessed_warnings_left', '', warnings_left, guesses,
                      remaining_letters, list_secret_word_dashes) 

        return (warnings_left, guesses)

    else:
        guesses -= 1

        central_print('already_guessed_guesses', '', warnings_left, guesses,
                      remaining_letters, list_secret_word_dashes) 

        return (warnings_left, guesses)

###############################################################################################################
def if_the_letter_has_not_yet_been_chosen(letter, guesses,
                                          secret_word):
    '''
    Checks if the chosen letter is a vowel or consonant and decreases
    the choices accordingly.
    '''
    if letter_is_in_secret_word(letter, secret_word):
        return guesses

    elif is_consonant(letter) and not letter_is_in_secret_word(letter, secret_word):
        guesses -= 1
        return guesses

    elif not is_consonant(letter) and not letter_is_in_secret_word(letter, secret_word):
        guesses -= 2
        return guesses
    
##############################################################################################################

def is_consonant(letter):
    '''
      check if the chosen letter is a consonant
    '''
    consonants = "bcdfghjklmnpqrstvwxyz"

    if letter in consonants:
      return True
    else:
      return False

#######################################################################################################

def letter_is_in_secret_word(letter, secret_word):
    '''
    check if the chosen letter is in the secret word
    '''
    
    if letter in secret_word:
        return True
    else:
        return False

#######################################################################################################

def unique_letters(secret_word):

    '''
    returns the number of unique letters of the secret word
    '''

    return len(set(secret_word))

###############################################################################################
def central_print(print_case, secret_word, 
                  warnings_left, guesses,
                  remaining_letters, list_secret_word_dashes):
    '''
    imprime o fluxo do jogo
    '''

    if print_case == 'presentation': # case 1

        print("Welcome to the game Hangman!")
        print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
        print("You have {} warnings left".format(warnings_left))
        print("---------------------")
        print("You have {} guesses left.".format(guesses))
        print("Available letters: {}".format(remaining_letters))

    elif print_case == 'good_guess': # case 2

        print("Good guess:", ''.join(list_secret_word_dashes))
        print("---------------------")
        print("You have {} guesses left.".format(guesses))
        print("Available letters: {}".format(remaining_letters))

    elif print_case == 'not_my_word': # case 3

        print("Oops! That letter is not in my word:", ''.join(list_secret_word_dashes))
        print("---------------------")
        print("You have {} guesses left.".format(guesses))
        print("Available letters: {}".format(remaining_letters))

    elif print_case == 'not_valid_caracter_warnings_left': # case 4

        print("Oops! That is not a valid letter. You have {} warnings left: {}".format(warnings_left, ' '.join(list_secret_word_dashes)))
        print("---------------------")
        print("You have {} guesses left.".format(guesses))
        print("Available letters: {}".format(remaining_letters))

    elif print_case == 'not_valid_caracter_guesses': # case 5

        print("Oops! That is not a valid letter. You have not warnings left so you lose one guesses: {}".format(' '.join(list_secret_word_dashes)))
        print("---------------------")
        print("You have {} guesses left.".format(guesses))
        print("Available letters: {}".format(remaining_letters))

    elif print_case == 'already_guessed_warnings_left': # case 6

        print("Oops! You've already guessed that letter. You have {} warnings left: {}".format(warnings_left, ' '.join(list_secret_word_dashes)))
        print("---------------------")
        print("You have {} guesses left.".format(guesses))
        print("Available letters: {}".format(remaining_letters))

    elif print_case == 'already_guessed_guesses': # case 7
  
        print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:{}".format(' '.join(list_secret_word_dashes)))
        print("---------------------")
        print("You have {} guesses left.".format(guesses))
        print("Available letters: {}".format(remaining_letters))

""" if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word) """

match_with_gaps("a_ ple", "apple")