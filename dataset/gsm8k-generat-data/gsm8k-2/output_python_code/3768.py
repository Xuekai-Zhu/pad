def solution():
    """Darnell has 1000 square feet of fabric that he's using to make mini flags. He makes square flags that are 4 feet by 4 feet,
     wide rectangular flags that are 5 feet by 3 feet, and tall rectangular flags that are 3 feet by 5 feet. 
     He has already made 16 square flags, 20 wide flags, and 10 tall flags. How many square feet of fabric does he have left?"""
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