def solution():
    # Calculate the area of the three 6-foot by 6-foot paintings
    area_large = 3 * 6 * 6

    # Calculate the area of the four 2-foot by 3-foot paintings
    area_small = 4 * 2 * 3

    # Calculate the area of the one 10-foot by 15-foot painting
    area_extra_large = 10 * 15

    # Calculate the total area of all the paintings
    total_area = area_large + area_small + area_extra_large
    result = total_area
    return result

print(solution())