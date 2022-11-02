def calculate_distance(x1, y1, x2, y2):
    first_figure = (x2 - x1)**2
    second_figure = (y2 - y1)**2
    result = (first_figure + second_figure)**0.5
    return round(result, 4)

