def solution():
    
    square_flag_size = 4 * 4
    wide_flag_size = 5 * 3
    tall_flag_size = 3 * 5
    square_flags_made = 16
    wide_flags_made = 20
    tall_flags_made = 10
    total_flags_made = square_flags_made + wide_flags_made + tall_flags_made
    total_fabric_used = (square_flags_made * square_flag_size) + (wide_flags_made * wide_flag_size) + (tall_flags_made * tall_flag_size)
    fabric_left = 1000 - total_fabric_used
    result = fabric_left
    return result

print(solution())