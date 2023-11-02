def solution():
    """Darnell has 1000 square feet of fabric that he's using to make mini flags. He makes square flags that are 4 feet by 4 feet, wide rectangular flags that are 5 feet by 3 feet, and tall rectangular flags that are 3 feet by 5 feet. He has already made 16 square flags, 20 wide flags, and 10 tall flags. How many square feet of fabric does he have left?"""
    # Define the areas of each type of flag
    SQUARE_FLAG_AREA = 16
    WIDE_FLAG_AREA = 15
    TALL_FLAG_AREA = 15

    # Define the number of each type of flag already made
    square_flags = 16
    wide_flags = 20
    tall_flags = 10

    # Calculate the total area of the flags already made
    total_area = square_flags * SQUARE_FLAG_AREA + wide_flags * WIDE_FLAG_AREA + tall_flags * TALL_FLAG_AREA

    # Calculate the remaining area of fabric
    remaining_area = 1000 - total_area

    # Display the remaining area of fabric
    result = remaining_area
    return result

print(solution())