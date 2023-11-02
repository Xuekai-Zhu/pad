def solution():
    hours_per_day = 8
    days_per_week = 7
    off_days = 2
    weeks_per_year = 52

    # Calculate the total number of training hours per week
    total_hours_per_week = (hours_per_day * (days_per_week - off_days))

    # Calculate the total number of training hours per year
    total_hours_per_year = total_hours_per_week * weeks_per_year

    result = total_hours_per_year
    return result

print(solution())