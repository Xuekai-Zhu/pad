def solution():
    
    shower_time = 10
    shower_frequency = 0.5  
    weeks = 4
    water_per_minute = 2
    total_showers = weeks * 7 * shower_frequency
    total_water_used = total_showers * shower_time * water_per_minute
    result = total_water_used
    return result

print(solution())