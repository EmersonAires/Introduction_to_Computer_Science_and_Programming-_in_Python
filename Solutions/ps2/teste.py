def letters_chosen_by_the_user():
    '''
      Returns the letters chosen by the user on each attempt
    '''

    n = 1
    letters_guessed = []

    while n < 7:
        letters_guessed.append(input("Insert the " + str(n) + "ª letter: "))
        n += 1
    
    print(letters_guessed)
    return letters_guessed



#letters_chosen_by_the_user()


if __name__ == "__main__":
    print("principal")
else:
    print("módulo")