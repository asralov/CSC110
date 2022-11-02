def get_height_category(sex, height):
    '''
    This program gets two parameters, first parameter gets the gender, is that male, female or unknown
    and the second parameter gets the height in inches in order to show the males or females height in general
    is that below average or above the average, if the first parameter does not suit the needed string
    then it shows unknown.
    sex: this parameter should be a string, and it should be equal to words 'female', 'male', and 'other input'
    height: this parameter should be an integer number in order to get the numbers to compare women's and men's height
    '''
    male = 'male'
    female = 'female'
    if sex == male:
        if height >= 70:
            above_average = 'above average'
            return above_average
        elif height <= 69:
            below_average = 'below average'
            return below_average
    elif sex == female:
        if height >= 64:
            above_average = 'above average'
            return above_average
        elif height <= 63:
            below_average = 'below average'
            return below_average
    else:
        unknown_average = 'unknown average'
        return unknown_average


