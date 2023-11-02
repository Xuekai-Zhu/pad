def solution():
    # Calculate the total area used by the flags already made
    square_flags_area = 16 * 4 * 4
    wide_flags_area = 20 * 5 * 3
    tall_flags_area = 10 * 3 * 5
    total_area_used = square_flags_area + wide_flags_area + tall_flags_area

    # Calculate the remaining fabric after making the flags
    total_fabric = 1000
    remaining_fabric = total_fabric - total_area_used
    result = remaining_fabric
    return result

print(solution())