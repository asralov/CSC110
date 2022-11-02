def count_vowels(str_list, num1, num2):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    string = str_list[num1: num2 + 1]
    for letter in string:
        if letter in vowels:
            count += 1
    return count


