def direct_selection(list):
    '''
    returns an ordered list
    '''
    end = len(list)
    for i in range(end - 1):
        #stores the position of the element to be compared
        min_position = i

        for j in range(i + 1, end):
            if list[j] < list[min_position]:
                min_position = j
        #change the position of the elements
        list[i], list[min_position] = list[min_position], list[i]
    
    return list

#################################################################

list = [2, 13, 9, 42, 3, 10]

print(direct_selection(list))