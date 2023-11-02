def solution():
    end_of_fourth_day = 34  # Depth of snowdrift at end of fourth day
    snow_on_third_day = 6  # Inches of snow added on third day
    snow_on_fourth_day = 18  # Inches of snow added on fourth day

    # Calculate the depth of snowdrift after the third day and before the fourth day
    after_third_day = end_of_fourth_day - snow_on_fourth_day
    before_fourth_day = after_third_day * 2

    # Calculate the depth of the drift on the first day
    depth_on_first_day = before_fourth_day - snow_on_third_day
    result = depth_on_first_day
    return result

print(solution())