# Abrorjon Asralov
# CSC110
# This program multiplies all numbers entered into a list

def multiply(numbers):
    result = 1
    i = 0
    while i < len(numbers):
        result *= numbers[i]

        i += 1
    return result


