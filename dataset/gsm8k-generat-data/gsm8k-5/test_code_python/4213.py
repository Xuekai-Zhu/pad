def solution():
    # Calculate the total area of the three squares of fabric
    area_first_square = 8 * 5
    area_second_square = 10 * 7
    area_third_square = 5 * 5
    total_area = area_first_square + area_second_square + area_third_square

    # Calculate the height of the flag given the total area and desired length
    height = total_area / 15
    result = height
    return result

print(solution())