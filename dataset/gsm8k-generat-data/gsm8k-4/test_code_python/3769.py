def solution():
    """Darnell has 1000 square feet of fabric that he's using to make mini flags. He makes square flags that are 4 feet by 4 feet, wide rectangular flags that are 5 feet by 3 feet, and tall rectangular flags that are 3 feet by 5 feet. He has already made 16 square flags, 20 wide flags, and 10 tall flags. How many square feet of fabric does he have left?"""
    # Define the size of the square flags
    square_flag_size = 4 * 4

    # Define the size of the tall rectangular flags
    tall_flag_size = 3 * 5

    # Define the size of the wide rectangular flags
    wide_flag_size = 5 * 3

    # Calculate the total size of the flags already made
    total_size_used = 16 * square_flag_size + 10 * tall_flag_size + 20 * wide_flag_size

    # Calculate the remaining fabric
    remaining_fabric = 1000 - total_size_used

    result = remaining_fabric
    return result

print(solution())