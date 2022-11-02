def differences(list1, list2):
    common_words = list1.intersection(list2)
    result = len(list1) + len(list2) - len(common_words)*2
    return (result)