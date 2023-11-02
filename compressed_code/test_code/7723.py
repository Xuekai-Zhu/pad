def solution():
    
    boxes = 10
    bottles_per_box = 50
    bottle_capacity = 12
    fill_percentage = 0.75
    total_liters = boxes * bottles_per_box * bottle_capacity * fill_percentage
    result = total_liters
    return result

print(solution())