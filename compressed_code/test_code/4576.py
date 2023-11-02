def solution():
    
    mix_time = 12
    bake_time = mix_time + 9
    cool_decorate_time = bake_time + 6
    total_time_per_cake = mix_time + bake_time + cool_decorate_time
    total_time_all_cakes = total_time_per_cake * 6
    hours = total_time_all_cakes / 60
    result = hours
    return result

print(solution())