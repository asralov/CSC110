import random
def count_characters():
    letter = random.randint('f','o','e', 'b')
    sentence = input()
    i = 0
    letters = 0
    while i <= len(sentence):
        if sentence[i] == letter:
            letters += 1
        i += 1
        print()


