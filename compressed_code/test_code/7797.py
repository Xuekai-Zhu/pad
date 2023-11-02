def solution():
    
    hourly_rate = 10
    days_per_week = 2
    hours_per_day = 3
    weeks_delivering = 6
    total_hours = days_per_week * hours_per_day * weeks_delivering
    total_money_earned = total_hours * hourly_rate
    result = total_money_earned
    return result

print(solution())