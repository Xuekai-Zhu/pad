def solution():
    # Calculate the total number of loose crayons
    loose_crayons = 5 + 27  # Francine has 5 loose crayons and her friend has 27 loose crayons
    
    # Calculate the number of crayons in each box
    crayons_per_box = 85 // 5  # Francine has five full boxes of crayons and a total of 85 crayons
    
    # Calculate the number of boxes needed for the loose crayons
    boxes_for_loose_crayons = (loose_crayons + crayons_per_box - 1) // crayons_per_box
    
    # Calculate the additional boxes needed for the loose crayons
    additional_boxes_needed = boxes_for_loose_crayons - 1 
    
    result = additional_boxes_needed
    return result

print(solution())