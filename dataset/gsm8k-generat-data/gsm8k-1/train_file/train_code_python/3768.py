def solution():
    """Darnell has 1000 square feet of fabric that he's using to make mini flags. He makes square flags that are 4 feet by 4 feet,
    wide rectangular flags that are 5 feet by 3 feet, and tall rectangular flags that are 3 feet by 5 feet. He has already made 16 square flags,
    20 wide flags, and 10 tall flags. How many square feet of fabric does he have left?"""
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