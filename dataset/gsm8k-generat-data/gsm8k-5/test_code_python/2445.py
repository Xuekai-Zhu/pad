def solution():
    eyes = 3
    wrinkles = 3 * eyes
    spots = 7 * wrinkles

    total_spots_and_wrinkles = spots + wrinkles
    difference = total_spots_and_wrinkles - eyes
    result = difference
    return result

print(solution())