def solution():
    
    box_capacity = 20
    full_boxes_percentage = 0.75
    half_boxes_percentage = 0.25
    total_boxes = 20
    full_boxes = total_boxes * full_boxes_percentage
    half_boxes = total_boxes * half_boxes_percentage
    total_parsnips = (full_boxes * box_capacity) + (half_boxes * (box_capacity/2))
    result = total_parsnips
    return result

print(solution())