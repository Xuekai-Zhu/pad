def solution():
    # Calculate the amount of runoff produced in one day
    daily_runoff = 24 * 1000

    # Calculate the number of days of rain the sewers can handle before overflowing
    days_before_overflow = 240000 / daily_runoff
    result = days_before_overflow
    return result

print(solution())