def insert_sort(list):
    '''
    Returns an ordered list
    '''
    n = len(list)
    for i in range(1, n):
        element = list[i]
        j = i
        while j > 0 and (list[j-1] > element):
            list[j] = list[j - 1]
            j = j - 1
        list[j] = element # insert the element
    
    return print(list)

####################################################

list = [5, 0, 7, 3, 1]
insert_sort(list)
