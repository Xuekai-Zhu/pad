def solution():
    
    first_half_hour_rain = 5
    second_half_hour_rain = 0.5 * first_half_hour_rain
    hour_rain = 0.5
    total_duration = 2
    total_rain = first_half_hour_rain + second_half_hour_rain + hour_rain
    average_rain = total_rain / total_duration
    result = average_rain
    return result

print(solution())