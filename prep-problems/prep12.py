# Abrorjon Asralov
# CSC 110
# This program shows the average result
# of the entered numbers

def average_numbers(num):
    i = 0
    total = 0
    while i < num:
        ask = int(input('Number:\n'))
        i += 1
        total += ask
    average = total/num
    print('Average =', round(average, 2))


