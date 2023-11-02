def solution():
    breaths_per_minute = 17
    air_inhaled_per_breath = 5/9
    minutes_in_a_day = 24 * 60
    total_air_inhaled = breaths_per_minute * air_inhaled_per_breath * minutes_in_a_day
    result = total_air_inhaled
    
    return result

print(solution())