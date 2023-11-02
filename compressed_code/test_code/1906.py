def solution():
    
    box_count = 10
    bottle_count = 50
    bottle_capacity = 12
    fill_ratio = 3/4
    total_liters = box_count * bottle_count * bottle_capacity * fill_ratio
    result = total_liters
    return result

print(solution())