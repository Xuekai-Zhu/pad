def solution():
    
    first_half_days = 15
    second_half_days = 30 - first_half_days
    first_half_rain = 4
    second_half_rain = first_half_rain * 2
    total_rain = (first_half_days * first_half_rain) + (second_half_days * second_half_rain)
    result = total_rain
    return result

print(solution())