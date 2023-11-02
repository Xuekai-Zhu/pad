def solution():
    
    water_temp = 41
    boil_temp = 212
    rate_of_increase = 3
    time_to_boil = (boil_temp - water_temp) / rate_of_increase
    pasta_cook_time = 12
    mix_time = pasta_cook_time / 3
    total_time = time_to_boil + pasta_cook_time + mix_time
    result = total_time
    return result

print(solution())