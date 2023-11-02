def solution():
    sticks_per_lollipop = 1
    sticks_needed = 400
    percent_complete = 0.6
    lollipops_per_week = 1 * 3  # Felicity goes to the store three times a week

    # Calculate the total number of lollipops Felicity has gotten so far
    total_lollipops = sticks_needed / sticks_per_lollipop / percent_complete

    # Calculate the number of weeks Felicity has been collecting lollipops
    num_weeks = total_lollipops / lollipops_per_week
    result = num_weeks
    return result

print(solution())