def solution():
    roses_given = 2 * 12  # Jordan gave Danielle two dozen roses
    chocolates_traded = 1 * 12  # Danielle traded the chocolates for another dozen roses
    total_roses = roses_given + chocolates_traded  # Total number of roses Danielle had

    # Calculate the number of roses that wilted on the first day
    wilted_first_day = total_roses / 2
    roses_left_first_day = total_roses - wilted_first_day  # Roses left after first day

    # Calculate the number of roses that wilted on the second day
    wilted_second_day = roses_left_first_day / 2
    roses_left_second_day = roses_left_first_day - wilted_second_day  # Roses left after second day

    result = roses_left_second_day
    return result

print(solution())