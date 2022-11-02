def two_words(list_of_words):
    words = list_of_words
    words.sort()
    for first_word in words:
        if first_word == words[0]:
            first = first_word
    for last_word in words:
        if last_word == words[len(words)-1]:
            last = last_word
    return first + ' ' + last





