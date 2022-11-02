def every_other(words):
    string = ''
    lists = words.split()
    for i in range(0, len(lists), 2):
        string = string + lists[i] + ' '
    return string
