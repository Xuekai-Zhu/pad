def solution():
    days_per_week = 5
    hours_per_day = 4
    hourly_rate = 5
    weekly_earning = days_per_week * hours_per_day * hourly_rate
    allocation = weekly_earning * 3/4
    result = allocation
    return result

print(solution())