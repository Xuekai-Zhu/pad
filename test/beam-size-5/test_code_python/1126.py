def solution():
    
    # Define the number of crayons and the weight of each box
    num_crayons = 200
    box_weight = 8

    # Calculate the total weight of all the crayons
    total_weight = num_crayons * box_weight

    # Calculate the weight of all the boxes
    num_boxes = num_crayons // 8
    if num_crayons % 8!= 0:
        num_boxes += 1

    # Calculate the total weight in pounds
    total_weight_pounds = num_boxes * 16

    # Display the total weight in pounds
    result = total_weight_pounds
    return result

print(solution())