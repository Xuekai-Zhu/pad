def solution():
    # Calculate the number of candy bars Nicole has
    nicole_bars = 16 + 4 + 5/2  # Kevin has 4 candy bars less than Nicole and Lena needs 5 more candy bars to have 3 times as many as Kevin
    # Calculate the number of candy bars Lena has
    lena_bars = 3 * (nicole_bars - 5)  # Lena needs 5 more candy bars to have 3 times as many as Kevin
    # Calculate the difference in candy bars between Lena and Nicole
    difference_bars = lena_bars - nicole_bars
    result = difference_bars
    return result

print(solution())