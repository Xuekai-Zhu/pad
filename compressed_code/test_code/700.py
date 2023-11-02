def solution():
    
    daily_requests = 6
    daily_completed = 4
    remaining = daily_requests - daily_completed
    remaining_after_5_days = remaining * 5
    result = remaining_after_5_days
    return result

print(solution())