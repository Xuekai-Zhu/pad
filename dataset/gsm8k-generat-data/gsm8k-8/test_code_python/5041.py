def solution():
    # Calculate the total area of the first 3 paintings
    area_first_3 = 3 * 5 * 5

    # Calculate the area of the fourth painting
    area_fourth = 10 * 8

    # Calculate the remaining area needed for the fifth painting
    remaining_area = 200 - area_first_3 - area_fourth

    # Calculate the width of the fifth painting
    width_fifth = remaining_area / 5
    result = width_fifth
    return result

print(solution())