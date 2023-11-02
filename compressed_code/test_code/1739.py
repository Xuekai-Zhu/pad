def solution():
    
    hourly_rate = 2
    hours_per_day = 4
    days_per_week = 3
    weeks = 4
    total_hours = hours_per_day * days_per_week * weeks
    total_earnings = total_hours * hourly_rate
    result = total_earnings
    return result

print(solution())