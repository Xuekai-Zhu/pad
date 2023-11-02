def solution():
    
    num_hives = 5
    liters_per_hive = 20
    total_liters = num_hives * liters_per_hive
    jars_needed = (total_liters/2) / 0.5
    result = jars_needed
    return result

print(solution())