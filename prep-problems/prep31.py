def get_elements(dictionary, integer):
    new_list = []
    for key in dictionary:
        if key[0].isupper():
            new_list.append(dictionary[key])
        elif key[len(key)-1].isupper():
            new_list.append(dictionary[key])
        elif dictionary[key] >= integer:
            new_list.append(dictionary[key])
    return new_list

