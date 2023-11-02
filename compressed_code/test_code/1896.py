def solution():
    
    brochures = 5000
    box_capacity = brochures / 5
    boxes_needed = brochures // box_capacity
    if brochures % box_capacity != 0:
        boxes_needed += 1
    result = boxes_needed
    return result

print(solution())