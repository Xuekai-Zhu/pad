def solution():
    
    total_brochures = 5000
    brochures_per_box = total_brochures / 5
    boxes_needed = total_brochures / brochures_per_box
    result = boxes_needed
    return result

print(solution())