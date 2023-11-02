def solution():
    computer_usage_last_week = 91  # Yella used the computer for 91 hours last week
    computer_usage_per_day = 8  # Yella plans to use the computer for 8 hours per day this week
    days_in_week = 7  # There are 7 days in a week

    # Calculate Yella's total planned computer usage for this week
    planned_usage_this_week = computer_usage_per_day * days_in_week

    # Calculate how much less Yella's computer usage is this week compared to last week
    difference = computer_usage_last_week - planned_usage_this_week
    result = difference
    return result

print(solution())