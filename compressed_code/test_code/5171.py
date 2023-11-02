def solution():
    
    days_worked = 10
    earnings_so_far = 250
    target_earnings = earnings_so_far * 2
    earnings_per_day = earnings_so_far / days_worked
    days_left = (target_earnings - earnings_so_far) / earnings_per_day
    result = days_left
    return result

print(solution())