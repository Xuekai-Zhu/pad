def solution():
    
    sewer_capacity = 240000
    hourly_runoff = 1000
    daily_runoff = hourly_runoff * 24
    days_until_overflow = sewer_capacity / daily_runoff
    result = days_until_overflow
    return result

print(solution())