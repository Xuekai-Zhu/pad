def solution():
    total_raisins = 437
    box_1_raisins = 72
    box_2_raisins = 74
    num_other_boxes = 3
    
    # Calculate the total number of raisins in the other three boxes
    total_other_boxes = total_raisins - (box_1_raisins + box_2_raisins)
    
    # Calculate the number of raisins in each of the other three boxes
    other_box_raisins = total_other_boxes / num_other_boxes
    
    result = other_box_raisins
    return result

print(solution())