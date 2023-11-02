def solution():
    """It starts raining at 7:00 and pours heavily until its stops at 17:00 on a particular day. On the second day, the rain takes 2 more hours than it took on the first day to stop. On the third day, the rain pours for twice the amount of time it took on the second day. Calculate the total time it was raining in the three days."""
    first_day_rain = 10  # rain from 7:00 to 17:00, 10 hours
    second_day_rain = first_day_rain + 2  # rain 2 hours more than first day
    third_day_rain = second_day_rain * 2  # rain twice as long as second day
    total_rain = first_day_rain + second_day_rain + third_day_rain
    result = total_rain
    return result

print(solution())