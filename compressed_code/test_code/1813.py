def solution():
    
    hourly_rate = 5
    hours_per_day = 5
    afternoons_per_week = 6
    weeks_babysitting = 7
    total_hours = hours_per_day * afternoons_per_week * weeks_babysitting
    total_earnings = total_hours * hourly_rate
    result = total_earnings
    return result

print(solution())