def solution():
    
    total_raisins = 437
    known_raisins = 72 + 74
    unknown_raisins = total_raisins - known_raisins
    num_other_boxes = 3
    raisins_per_box = unknown_raisins / num_other_boxes
    result = raisins_per_box
    return result

print(solution())