def solution():
    
    num_boxes = 4
    num_eggs_per_box = 12 // num_boxes
    remaining_eggs = 12 - num_eggs_per_box
    remaining_weight = remaining_eggs * 10
    result = remaining_weight
    return result

print(solution())