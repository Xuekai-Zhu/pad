def solution():
    days_per_week = 7
    rain_days = 3
    snow_days = 4
    minutes_per_day = 60
    rain_speed = 30
    snow_speed = 10
    total_miles = (rain_days * rain_speed) + (snow_days * snow_speed)
    result = total_miles
    return result

print(solution())