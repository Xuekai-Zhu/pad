def solution():
    # Calculate the number of red stripes on each flag
    total_stripes = 13  # total number of stripes on each flag
    red_stripes = 1 + (total_stripes - 1) // 2  # first stripe is red, half of the remaining stripes are also red
    # Calculate the total number of red stripes on all flags
    total_red_stripes = red_stripes * 10  # John buys 10 flags
    result = total_red_stripes
    return result

print(solution())