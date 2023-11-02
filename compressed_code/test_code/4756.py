def solution():
    
    normal_time_per_barrel = 3
    leaky_time_per_barrel = 5
    barrels_to_fill = 12
    normal_total_time = normal_time_per_barrel * barrels_to_fill
    leaky_total_time = leaky_time_per_barrel * barrels_to_fill
    extra_time = leaky_total_time - normal_total_time
    result = extra_time
    return result

print(solution())