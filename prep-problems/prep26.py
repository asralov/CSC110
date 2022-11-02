def longest_word(str_of_words):
    word = str_of_words.split()
    long_word = max(word, key=len)
    return long_word


