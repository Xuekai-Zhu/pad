def solution():
    
    square_flag_area = 4 * 4
    wide_flag_area = 5 * 3
    tall_flag_area = 3 * 5
    square_flags = 16
    wide_flags = 20
    tall_flags = 10
    total_flags = square_flags + wide_flags + tall_flags
    total_area_used = (square_flag_area * square_flags) + (wide_flag_area * wide_flags) + (tall_flag_area * tall_flags)
    total_area_left = 1000 - total_area_used
    result = total_area_left
    return result

print(solution())