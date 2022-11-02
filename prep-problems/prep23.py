def get_supply_count():
    count = 0
    supplies = open('supplies.txt', 'r')
    lines = supplies.readlines()
    for i in lines:
        index = i.find(' ')
        number = int(i[index+1: ])
        count += number

    result = open('total.txt', 'w')
    result.write(str(count))
