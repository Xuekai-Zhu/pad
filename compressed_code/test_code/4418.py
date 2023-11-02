def solution():
    
    tissues_per_box = 160
    num_boxes = 3
    total_tissues = tissues_per_box * num_boxes
    used_tissues = 210
    remaining_tissues = total_tissues - used_tissues
    result = remaining_tissues
    return result

print(solution())