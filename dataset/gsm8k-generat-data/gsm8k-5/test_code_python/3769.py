def solution():
    # Calculate the total area used by the square flags
    area_square_flags = 16 * (4 ** 2)

    # Calculate the total area used by the wide flags
    area_wide_flags = 20 * (5 * 3)

    # Calculate the total area used by the tall flags
    area_tall_flags = 10 * (3 * 5)

    # Calculate the total area used by all the flags
    total_area_used = area_square_flags + area_wide_flags + area_tall_flags

    # Calculate the amount of fabric remaining
    fabric_remaining = 1000 - total_area_used
    result = fabric_remaining
    return result

print(solution())