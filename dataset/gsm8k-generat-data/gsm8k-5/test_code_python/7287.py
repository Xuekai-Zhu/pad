def solution():
    kevin_candy_bars = (16+5)/3 - 5  # Kevin has 4 candy bars less than Nicole, and Lena has 5 more candy bars than Kevin
    nicole_candy_bars = kevin_candy_bars + 4
    lena_candy_bars = 16

    # Calculate the difference in candy bars between Lena and Nicole
    difference = lena_candy_bars - nicole_candy_bars
    result = difference
    return result

print(solution())