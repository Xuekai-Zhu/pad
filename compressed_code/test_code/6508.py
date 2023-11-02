def solution():
    
    daily_requests = 6
    requests_worked_on = 4
    remaining_requests_per_day = daily_requests - requests_worked_on
    remaining_requests_after_5_days = remaining_requests_per_day * 5
    result = remaining_requests_after_5_days
    return result

print(solution())