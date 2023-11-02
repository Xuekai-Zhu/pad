def solution():
    """Every day, Bob logs 10 hours of work in his office. If he works for five days a week, calculate the total number of hours he logs in a month."""
    daily_hours = 10
    work_days_per_week = 5
    work_days_per_month = 4 # assuming four weeks in a month
    total_hours = daily_hours * work_days_per_week * work_days_per_month
    result = total_hours
    return result

print(solution())