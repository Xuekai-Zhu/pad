def solution():
    
    breaths_per_minute = 17
    air_per_breath = 5/9
    minutes_per_day = 24 * 60
    total_breaths = breaths_per_minute * minutes_per_day
    total_air = total_breaths * air_per_breath
    result = total_air
    return result

print(solution())