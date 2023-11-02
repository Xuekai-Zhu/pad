def solution():
    
    barrel_size = 220
    leak_percentage = 0.1
    remaining_percentage = 1 - leak_percentage
    remaining_liters = remaining_percentage * barrel_size
    result = remaining_liters
    return result

print(solution())