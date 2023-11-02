def solution():
    
    rain_distance = 30
    snow_distance = 10
    rain_frequency = 3
    snow_frequency = 4
    minutes_per_hour = 60
    total_rain_distance = rain_distance * rain_frequency * minutes_per_hour / 20
    total_snow_distance = snow_distance * snow_frequency * minutes_per_hour / 20
    total_distance = total_rain_distance + total_snow_distance
    result = total_distance
    return result

print(solution())