def solution():
    
    initial_temp = 41
    boiling_temp = 212
    temp_increase_per_minute = 3
    time_to_boil = (boiling_temp - initial_temp) / temp_increase_per_minute
    time_to_cook_pasta = 12
    time_to_mix_and_make_salad = time_to_cook_pasta / 3
    total_time = time_to_boil + time_to_cook_pasta + time_to_mix_and_make_salad
    result = total_time
    return result

print(solution())