def solution():
    # Calculate the ratio of grey stones to green stones in the separate collection
    grey_to_green = 40 / 60

    # Calculate the number of white stones in relation to the number of black stones in the first collection
    white_to_black = grey_to_green / (1 - grey_to_green)

    # Calculate the total number of stones in the first collection
    total_stones = 100

    # Calculate the number of white stones based on the ratio and the fact that there are more white stones than black stones
    white_stones = round((total_stones / (white_to_black + 1 + 1)) * white_to_black)

    result = white_stones
    return result

print(solution())