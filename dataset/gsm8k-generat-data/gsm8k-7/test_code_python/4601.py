def solution():
    weekly_hours = 4
    num_months = 5
    weeks_per_month = 4

    # Calculate the total number of weeks in five months
    total_weeks = num_months * weeks_per_month

    # Calculate the total number of hours Reese will practice
    total_hours = weekly_hours * total_weeks
    result = total_hours
    return result

print(solution())