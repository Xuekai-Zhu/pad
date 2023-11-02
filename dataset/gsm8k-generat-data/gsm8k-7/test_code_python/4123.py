def solution():
    total_units = 42
    total_area = 5040
    num_small_units = total_units - 20
    area_of_small_units = 8 * 4 * 20
    area_of_remaining_units = (total_area - area_of_small_units) / num_small_units
    result = area_of_remaining_units
    return result

print(solution())