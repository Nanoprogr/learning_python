def remove_first_and_last_element(list_to_clean):
    list_clean = [x for x in list_to_clean[1:-2]]
    print(list_clean)

list_to_clean = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

remove_first_and_last_element(list_to_clean)