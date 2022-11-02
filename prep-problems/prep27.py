def get_gpa(cs_classes):
    cs120 = cs_classes.get('cs120')
    cs210 = cs_classes.get('cs210')
    cs245 = cs_classes.get('cs245')
    sum_of_gpa = cs120 + cs210 + cs245
    result = sum_of_gpa/3
    return result


