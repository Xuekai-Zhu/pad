def solution():
    
    initial_weight = 50000
    first_unload_percent = 10
    first_unload_weight = initial_weight * (first_unload_percent / 100)
    remaining_weight = initial_weight - first_unload_weight
    second_unload_percent = 20
    second_unload_weight = remaining_weight * (second_unload_percent / 100)
    final_weight = remaining_weight - second_unload_weight
    result = final_weight
    return result

print(solution())