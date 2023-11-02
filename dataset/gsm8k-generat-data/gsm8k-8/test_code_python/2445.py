def solution():
    # Calculate the number of wrinkles and eyes
    eyes = 3
    wrinkles = 3 * eyes

    # Calculate the number of spots
    spots = 7 * wrinkles

    # Calculate the total number of spots and wrinkles
    total_spots_wrinkles = spots + wrinkles

    # Calculate the difference between the number of eyes and the total number of spots and wrinkles
    difference = total_spots_wrinkles - eyes
    result = difference
    return result

print(solution())