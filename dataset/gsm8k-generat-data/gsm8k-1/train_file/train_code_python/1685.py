def solution():
    """Every day, Bob logs 10 hours of work in his office. If he works for five days a week, calculate the total number of hours he logs in a month."""
    hours_per_day = 10
    days_per_week = 5
    weeks_per_month = 4
    total_hours = hours_per_day * days_per_week * weeks_per_month
    result = total_hours
    return result

print(solution())