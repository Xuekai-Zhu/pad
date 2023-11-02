def solution():
    total_carrots = 300
    used_before_lunch = 2/5 * total_carrots

    # Calculate the remaining number of carrots after lunch
    remaining_carrots = total_carrots - used_before_lunch

    # Calculate the number of carrots used at the end of the day
    used_end_of_day = 3/5 * remaining_carrots

    # Calculate the number of carrots not used that day
    not_used = remaining_carrots - used_end_of_day
    result = not_used
    return result

print(solution())