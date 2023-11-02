def solution():
    
    wage_per_hour = 5
    hours_per_day = 5
    afternoons_per_week = 6
    weeks = 7
    total_hours = hours_per_day * afternoons_per_week * weeks
    total_earnings = total_hours * wage_per_hour
    result = total_earnings
    return result

print(solution())