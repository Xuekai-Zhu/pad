def solution():
    # Calculate the initial number of roses
    initial_roses = 2*12 + 1*12  # two dozen roses and another dozen roses traded for the chocolates
    # Calculate the number of roses that wilted on the first day
    wilted_first_day = initial_roses / 2
    # Calculate the number of roses remaining after the first day
    remaining_first_day = initial_roses - wilted_first_day
    # Calculate the number of roses that wilted on the second day
    wilted_second_day = remaining_first_day / 2
    # Calculate the number of unwilted flowers remaining
    remaining_roses = remaining_first_day - wilted_second_day
    result = remaining_roses
    return result

print(solution())