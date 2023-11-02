def solution():
    total_fabric = 1000

    # Calculate the fabric used for square flags
    num_square_flags = 16
    square_flag_fabric = 4 * 4 * num_square_flags

    # Calculate the fabric used for wide rectangular flags
    num_wide_flags = 20
    wide_flag_fabric = 5 * 3 * num_wide_flags

    # Calculate the fabric used for tall rectangular flags
    num_tall_flags = 10
    tall_flag_fabric = 3 * 5 * num_tall_flags

    # Calculate the total fabric used for all flags
    total_flag_fabric = square_flag_fabric + wide_flag_fabric + tall_flag_fabric

    # Calculate the fabric remaining
    fabric_remaining = total_fabric - total_flag_fabric
    result = fabric_remaining
    return result

print(solution())