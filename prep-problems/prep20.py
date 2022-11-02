def grade_info(grades):
    for max_grade_is in grades:
        max_grade = max(grades)
    for min_grade_is in grades:
        min_grade = min(grades)
    result = 0
    index = 0
    for average in grades:
        result += grades[index]
        index += 1
    average_grade = result/index

    return max_grade, min_grade, average_grade

