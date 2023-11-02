def solution():
    hourly_rate = 5
    hours_per_day = 5
    days_per_week = 6
    weeks_worked = 7
    total_hours = hours_per_day * days_per_week * weeks_worked
    total_earnings = hourly_rate * total_hours
    result = total_earnings
    return result

print(solution())