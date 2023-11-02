def solution():
    
    total_raisins = 437
    box1_raisins = 72
    box2_raisins = 74
    sum_of_other_boxes = total_raisins - box1_raisins - box2_raisins
    num_of_other_boxes = 3
    raisins_per_other_box = sum_of_other_boxes / num_of_other_boxes
    result = raisins_per_other_box
    return result

print(solution())