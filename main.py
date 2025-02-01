def isSublist(larger_list, smaller_list):
    is_sub = False
    for item in range(len(larger_list) - len(smaller_list) + 1):
        if larger_list[item : item + len(smaller_list)] == smaller_list:
            is_sub = True
            break
    return is_sub

list_1 = []
list_2 = []

user_1 = input('Insert a value for the list 1 (empty to stop): ')
while user_1 != '':
    list_1.append(user_1)
    user_1 = input('Insert a value for the list 1 (empty to stop): ')

user_2 = input('Insert a value for the list 2 (empty to stop): ')
while user_2 != '':
    list_2.append(user_2)
    user_2 = input('Insert a value for the list 2 (empty to stop): ')    

if len(list_1) >= len(list_2):
    if isSublist(list_1, list_2):
        print ('list 2 is a sublist of list 1')

    else:
        print ('list 2 is not a sublist of list 1')
else:
    if isSublist(list_2, list_1):
        print ('list 1 is a sublist of list 2')

    else:
        print ('list 1 is not a sublist of list 2')
