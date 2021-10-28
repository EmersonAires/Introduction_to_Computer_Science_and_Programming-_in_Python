# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : Emerson Eduardo Aires Nunes
# Collaborators : None
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


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

    print()
    print("------------------------------------------------------")
    print()


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
    
    first_component = sum_of_the_points_for_letters_in_the_word(word)
    second_component = ((7 * len(word)) - 3 * (n - len(word)))

    if second_component < 1:
        second_component = 1
    
    return first_component * second_component


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
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line


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
    
    hand={}
    num_vowels = int(math.ceil((n / 3)))

    for i in range(num_vowels - 1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    hand['*'] = 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

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

    update_hand = hand.copy()
    freq_letter_in_the_word = get_frequency_dict(word.lower())

    for key in update_hand.keys():
        if key in freq_letter_in_the_word.keys():
            update_hand[key] = (update_hand[key] - freq_letter_in_the_word[key])
    
    for key in update_hand.keys():
        if update_hand[key] < 0:
            update_hand[key] = 0
    
    return update_hand


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
    word = word.lower()
    freq_word = get_frequency_dict(word)
    hand_copy = hand.copy()
    valid_word = True

    # if the wildcard character is in the word
    if word.find("*") != -1:
        if check_list_of_word_combinations(possible_words_using_wildcard(word)):

            valid_word = check_letters_in_the_word(freq_word,
                                                   hand_copy,
                                                   valid_word)
            return valid_word

        else: # not this valid word list
            valid_word = False
            return valid_word

    else:

        if word not in word_list:
            valid_word = False
            return valid_word
        
        valid_word = check_letters_in_the_word(freq_word,
                                               hand_copy,
                                               valid_word)
          
    return valid_word


def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    
    number_of_letters = 0
    for key in hand.keys():
        number_of_letters += hand[key]
    
    return number_of_letters

def play_hand(hand,
              word_list,
              option_substitute_letter,
              option_replay_hand,
              block_substitute_letter=False
              ):

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


    copy_hand = hand.copy()
    total_score = 0
    number_of_letters_in_current_hand = calculate_handlen(copy_hand)

    # asks if the user wants to replace a letter
    if option_substitute_letter and not block_substitute_letter:
        input_substitute_letter = input("Would you like to substitute a letter? ")

        print()
        print("------------------------------------------------------")
        print()

        if input_substitute_letter == "yes":
            letter = input("Which letter would you like to replace: ")
            copy_hand = substitute_hand(hand, letter)
            option_substitute_letter = False


    # As long as there are still letters left in the hand:
    while number_of_letters_in_current_hand != 0:
        # Display the hand
        print("Current Hand: ", sep="") 
        display_hand(copy_hand)

        # Ask user for input
        word = input("Enter word, or '!!' to indicate that you are finished: ")

        # If the input is two exclamation points:
        if word == "!!":
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not two exclamation points):
        else:

            # If the word is valid:
            if is_valid_word(word, copy_hand, word_list):
                # Tell the user how many points the word earned,
                # and the updated total score
                points = get_word_score(word,
                                        number_of_letters_in_current_hand)

                total_score += points

                print("{} earned {} points. Total: {} points".format(
                                                                     word,
                                                                     points,
                                                                     total_score
                                                                    ))
                print()
                print("------------------------------------------------------")
                print()
         
                
            # Otherwise (the word is not valid):
            # Reject invalid word (print a message)
            else:
                print("That is not a valid word. Please choose another word.")
                print()
                print("------------------------------------------------------")
                print()
        
            # update the user's hand by removing the letters of their inputted word
            copy_hand = update_hand(copy_hand, word)
            number_of_letters_in_current_hand = calculate_handlen(copy_hand)

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    if word == "!!":
        print("Total score for this hand: {}".format(total_score))

        print()
        print("------------------------------------------------------")
        print()

    if number_of_letters_in_current_hand == 0:
        print("Ran out of letters. Total score for this hand: {}".format(total_score))

        print()
        print("------------------------------------------------------")
        print()

    # ask the user if he wants to repeat the hand
    if option_replay_hand:
        input_replay_hand = input("Would you like to replay the hand? ")

        print()
        print("------------------------------------------------------")
        print()

        if input_replay_hand == "yes":
            option_replay_hand = False
            block_substitute_letter = True

            (total_score,
             option_substitute_letter,
             option_replay_hand) = play_hand(hand,
                                             word_list,
                                             option_substitute_letter,
                                             option_replay_hand,
                                             block_substitute_letter
                                             )
            



    # Return the total score as result of function
    return total_score, option_substitute_letter, option_replay_hand


def substitute_hand(hand, letter):
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
    

    while True:
      
        new_letter = random.choice(alphabet)
        
        if new_letter not in hand.keys():
            break
    
    hand[new_letter] = hand.get(letter)
    
    hand.pop(letter)

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
    total_score_for_this_hand = 0
    total_score_over_all_hands = 0
    option_substitute_letter = True
    option_replay_hand = True

    number_of_hands = int(input("Enter total number of hands: "))


    while number_of_hands > 0:

        dic = {2:{'a':1, 'c':1, 'i': 1, '*':1, 'p':1, 'r':1, 't':1}, 1:{'d':2, '*':1, 'l':1, 'o':1, 'u':1, 't':1}}
        hand = deal_hand(HAND_SIZE)

        print("Current Hand: ", sep="") 
        display_hand(hand)

        (total_score_for_this_hand,
         option_substitute_letter,
         option_replay_hand) = play_hand(hand,
                                         word_list,
                                         option_substitute_letter,
                                         option_replay_hand
                                         )
        
        total_score_over_all_hands += total_score_for_this_hand

        number_of_hands -= 1

    print("Total score over all hands: {}".format(total_score_over_all_hands))
    print()
    print("------------------------------------------------------")
    print()


def sum_of_the_points_for_letters_in_the_word(word):
    '''
    Return the sum of the points for letters in the word
    '''
    sum_of_the_points = 0
    word = word.lower()

    try:
        for letter in word:
            sum_of_the_points += SCRABBLE_LETTER_VALUES.get(letter, 0)
    except KeyError:
        pass 

    """  # add 1 point for the wildcard
    if word.find("*") != -1:
        sum_of_the_points += 1  
    """

    return sum_of_the_points


def check_letters_in_the_word(freq_word, hand_copy, valid_word):
    '''
    checks if all letters of the word are part of the hand and the amount.
    '''
    
    # check that all letters of the word are part of the hand 
    for key in freq_word.keys():
        if key not in hand_copy.keys():
            valid_word = False
            return valid_word
        else:
            hand_copy[key] = (hand_copy[key] - freq_word[key])

    # check if the number of letters in the word is greater than in the hand
    for key in hand_copy.keys():
        if hand_copy[key] < 0:
            valid_word = False
            return valid_word


    return valid_word

def possible_words_using_wildcard(word):
    '''
    returns a list of possible words formed using the wildcard
    '''
    list_letters_in_word = list(word)
    positon_wildcard = word.find("*")
    list_possible_words = []

    for wowel in VOWELS:
        list_letters_in_word[positon_wildcard] = wowel
        combined_word_= ''.join(list_letters_in_word)
        list_possible_words.append(combined_word_)
    
    return list_possible_words


def check_list_of_word_combinations(list_possible_words):
    '''
    check if there is a valid word in the received list.

    return: Bolean
    '''
      
    valid_word = False
    for word in list_possible_words:
        if word in word_list:
            valid_word = True
            return valid_word
    
    return valid_word


if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
