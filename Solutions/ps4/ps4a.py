# Problem Set 4A
# Name: Emerson Eduardo Aires Nunes
# Collaborators: None
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    # case base
    if len(sequence) == 1:
        return list(sequence)

    else:
        # reduce the string
        first_character = sequence[0]
        remaining_characters = sequence[1:]

        # recursion
        permutation_list = get_permutations(remaining_characters)

        new_permutation_list = []
        element_length = len(permutation_list[0]) + 1

        for string in permutation_list:
            position_string = 0
            position_first_character = 0
            list_character = []
            number_of_elements_new_per_element = (len(permutation_list[0]) + 1) 

            # new permutations formed by each string in the permutation_list list
            while number_of_elements_new_per_element > 0:
                # formation of each new string
                for i in range(element_length):
                    if i == position_first_character:
                        list_character.append(first_character)
                    else:
                        list_character.append(string[position_string])
                        position_string += 1

                position_first_character += 1
                position_string = 0
                
                element_string = ''.join(list_character)
                # adding the new string
                new_permutation_list.append(element_string)

                list_character = []
                number_of_elements_new_per_element -= 1

        return new_permutation_list


if __name__ == '__main__':
    #EXAMPLE 1
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

    print()
    print('----------------------------------------------------------------------------------------------')
    print()
    #EXAMPLE 2
    example_input = 'you'
    print('Input:', example_input)
    print('Expected Output:', ['you', 'oyu', 'ouy', 'yuo', 'uyo', 'uoy'])
    print('Actual Output:', get_permutations(example_input))

    print()
    print('----------------------------------------------------------------------------------------------')
    print()
    #EXAMPLE 3
    example_input = 'one'
    print('Input:', example_input)
    print('Expected Output:', ['one', 'noe', 'neo', 'oen', 'eon', 'eno'])
    print('Actual Output:', get_permutations(example_input))