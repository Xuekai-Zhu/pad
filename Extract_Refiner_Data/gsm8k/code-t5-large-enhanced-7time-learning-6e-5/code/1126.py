def solution():
    
    # Define the number of crayons and the weight per crayon in ounces
    NUM_CRAYONS = 200
    CRAYON_WEIGHT_PER_CRAYON = 1

    # Calculate the number of boxes and crayons
    num_boxes = NUM_CRAYONS // 8
    num_crayons = NUM_CRAYONS - num_boxes

    # Calculate the total weight of the boxes and crayons
    total_weight = num_boxes * CRAYON_WEIGHT_PER_CRAYON * 16

    # Display the total weight
    result = total_weight
    return result

print(solution())