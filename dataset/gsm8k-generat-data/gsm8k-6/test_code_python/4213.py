def solution():
    # Calculate the total area of the three squares
    area_square1 = 8 * 5
    area_square2 = 10 * 7
    area_square3 = 5 * 5
    total_area = area_square1 + area_square2 + area_square3

    # Calculate the height of the flag
    height = total_area / 15
    result = height
    return result

print(solution())