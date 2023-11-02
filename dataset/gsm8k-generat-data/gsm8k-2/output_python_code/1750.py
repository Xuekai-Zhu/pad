def solution():
    """The sewers in Middleton can handle 240,000 gallons of run-off. Each hour of rain produces 1000 gallons of runoff. How many days of rain can the sewers handle before they overflow?"""
    sewer_capacity = 240000
    hourly_runoff = 1000
    daily_runoff = hourly_runoff * 24
    days_until_overflow = sewer_capacity / daily_runoff
    result = days_until_overflow
    return result

print(solution())