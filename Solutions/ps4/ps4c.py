# Problem Set 4C
# Name: Emerson Eduardo Aires Nunes
# Collaborators: None
# Time Spent: 24 days

import string
import random
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'
VALID_WORDS = load_words(WORDLIST_FILENAME)

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = VALID_WORDS

    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        copy_valid_words = VALID_WORDS[:]
        return copy_valid_words
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        
        transpose_dict = {}
        i = 0
        for vowel in VOWELS_LOWER:
            transpose_dict[vowel] = vowels_permutation[i]
            i += 1
        
        i = 0
        for vowel in VOWELS_UPPER:
            transpose_dict[vowel] = vowels_permutation[i].upper()
            i += 1
        
        for consoant in CONSONANTS_LOWER:
            transpose_dict[consoant] = consoant

        for consoant in CONSONANTS_UPPER:
            transpose_dict[consoant] = consoant
        
        return transpose_dict

    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        
        message_text = self.get_message_text()
        encrypted_message = ''

        for caracter in message_text:
            try:
                encrypted_message += transpose_dict[caracter]
            except:
                encrypted_message += caracter

        return encrypted_message

        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = VALID_WORDS

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        permutation_list = get_permutations('aeiou')
        qtd_valid_words = 0
        dic_transpose = {}
        key_best_valid_words = None
        best_valid_words = 0
        
        i = 0
        # stores the number of valid words and text in a dictionary.
        for permutation in permutation_list:
            transpose_dic = self.build_transpose_dict(permutation)
            transpose_message = self.apply_transpose(transpose_dic)
            qtd_valid_words = number_of_valid_words(transpose_message)
            dic_transpose[i] = (qtd_valid_words, transpose_message)

            i += 1

        # scrolls through the dictionary and checks as many valid words   
        for key in dic_transpose.keys():
            if dic_transpose[key][0] > best_valid_words:
                best_valid_words = dic_transpose[key][0]
                key_best_valid_words = key

        if key_best_valid_words == None:
            return self.get_message_text()
        else:
            return dic_transpose[key_best_valid_words][1]

def number_of_valid_words(transpose_message):
    '''
    check the number of valid words in a message
    '''

    word_list = transpose_message.split(' ')
    valid_words_count = 0

    for word in word_list:
        if is_word(VALID_WORDS, word):
            valid_words_count += 1
    
    return valid_words_count


if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())

    print('--------------------------------------------------------')

    # Example test case
    message = SubMessage("How are you?")
    permutation = "eauio"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hiw era yio?")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())


    print('--------------------------------------------------------')

    # Example test case
    message = SubMessage("Apple Word Bad")
    permutation = "aeoui"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Apple Wurd Bad")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())

    print('--------------------------------------------------------')

    # Example test case
    message = SubMessage("How do you do?")
    permutation = "eauio"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hiw di yio di?")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
