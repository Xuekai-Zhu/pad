def solution():
    
    days_per_week = 5
    hours_per_day = 4
    hourly_rate = 5
    weekly_earnings = days_per_week * hours_per_day * hourly_rate
    allocation_proportion = 3 / 4
    allocation_amount = weekly_earnings * allocation_proportion
    result = allocation_amount
    return result

print(solution())