def solution():
    sewer_capacity = 240000
    hourly_runoff = 1000
    daily_runoff = hourly_runoff * 24  # 24 hours in a day

    # Calculate the number of days before the sewers reach capacity
    days_until_overflow = sewer_capacity // daily_runoff
    result = days_until_overflow
    return result

print(solution())