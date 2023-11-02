def solution():
    
    shirts_per_load = 5 // 1
    pants_per_load = 5 // 2
    total_shirts = 20
    total_pants = 20
    total_weight = (total_shirts // 4 + total_pants // 2)
    total_loads = (total_weight + shirts_per_load - 1) // shirts_per_load
    result = total_loads
    return result

print(solution())