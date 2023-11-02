def solution():
    # Calculate the total length of rope needed in inches
    total_length = 10 * 6  

    # Calculate the cost of the 6-foot rope
    six_foot_cost = 5  

    # Calculate the cost of the 1-foot rope
    one_foot_cost = 1.25  

    # Calculate the number of 1-foot ropes needed
    num_one_foot = total_length / 12  

    # Round up to get the total number of 1-foot ropes needed
    total_one_foot = math.ceil(num_one_foot)  

    # Calculate the total cost of the 1-foot ropes
    one_foot_total_cost = total_one_foot * one_foot_cost  

    # Compare the cost of the 6-foot rope and the 1-foot ropes
    if six_foot_cost < one_foot_total_cost:
        result = six_foot_cost  
    else:
        result = one_foot_total_cost
    return result

print(solution())