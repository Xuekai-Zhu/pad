def solution():
    total_brochures = 5000
    brochures_per_box = total_brochures / 5
    total_boxes = total_brochures / brochures_per_box
    result = total_boxes
    return result

print(solution())