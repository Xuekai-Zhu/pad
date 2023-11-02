def solution():
    """Lena has 16 candy bars. She needs 5 more candy bars to have 3 times as many as Kevin, and Kevin has 4 candy bars less than Nicole. How many more candy bars does Lena have than Nicole?"""
    # Define Lena's starting number of candy bars
    lena_bars = 16

    # Calculate the number of candy bars Kevin has
    kevin_bars = (lena_bars + 5) / 3 - 5

    # Calculate the number of candy bars Nicole has
    nicole_bars = kevin_bars + 4

    # Calculate the difference in candy bars between Lena and Nicole
    difference = lena_bars - nicole_bars

    # Display the difference in candy bars
    result = difference
    return result

print(solution())