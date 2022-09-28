def calculate_tree_height(height, years):
    i = 0
    while i < years:
        i += 1
        height *= 1.2
    return round(height, 4)


#print(calculate_tree_height(5,15))


