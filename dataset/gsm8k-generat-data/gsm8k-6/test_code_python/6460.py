def solution():
    # Find the percentage of grey and green stones in the separate collection
    grey_percentage = 40/100
    green_percentage = 60/100

    # Find the number of white stones in Brian's collection
    total_white_black_stones = 100 - (40 + 60)  # number of white and black stones combined
    white_percentage = (grey_percentage + green_percentage) / 2  # percentage of white stones
    white_stones = total_white_black_stones * white_percentage  # number of white stones
    if white_stones > total_white_black_stones/2:  # check if there are more white stones than black stones
        result = white_stones
    else:
        result = 'Error: There are not more white stones than black stones.'
    return result

print(solution())