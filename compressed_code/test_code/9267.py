def solution():
    
    initial_rain = 2
    rain_from_2_to_4 = 4 * 2
    rain_from_4_to_7 = 3 * 3
    rain_from_7_to_9 = 0.5 * 2
    total_rain = initial_rain + rain_from_2_to_4 + rain_from_4_to_7 + rain_from_7_to_9
    result = total_rain
    return result

print(solution())