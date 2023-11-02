def solution():
    current_height = 10  # in feet
    growth_rate_per_week = 2  # in feet
    weeks_in_month = 4
    months = 4

    # Calculate the total number of weeks in the given number of months
    total_weeks = weeks_in_month * months

    # Calculate the total growth in height during the given number of weeks
    total_growth = growth_rate_per_week * total_weeks

    # Calculate the final height of the tree
    final_height = current_height + total_growth
    result = final_height
    return result

print(solution())