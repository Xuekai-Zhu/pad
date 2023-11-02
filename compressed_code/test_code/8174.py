def solution():
    
    shirts_per_load = 5 // 1 * 4
    pants_per_load = 5 // 1 * 2
    total_shirts = 20
    total_pants = 20
    total_loads = (total_shirts // shirts_per_load) + (total_pants // pants_per_load)
    result = total_loads
    return result

print(solution())