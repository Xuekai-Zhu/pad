def solution():
    
    milk_per_milkshake = 4
    ice_cream_per_milkshake = 12
    total_milkshakes = min(72 // milk_per_milkshake, 192 // ice_cream_per_milkshake)
    total_milk_used = total_milkshakes * milk_per_milkshake
    milk_leftover = 72 - total_milk_used
    result = milk_leftover
    return result

print(solution())