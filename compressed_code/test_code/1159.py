def solution():
    
    load = 50000
    first_unload = 0.1 * load
    remaining_load = load - first_unload
    second_unload = 0.2 * remaining_load
    final_load = remaining_load - second_unload
    result = final_load
    return result

print(solution())