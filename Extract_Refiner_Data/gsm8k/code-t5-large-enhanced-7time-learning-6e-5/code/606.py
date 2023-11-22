def solution():
    
    # Define the cost per meter and the length of Monica's street
    COST_PER_METER = 198
    MONICA_LENGTH = 150

    # Calculate the length of Lewis' street
    LEWIS_LENGTH = 490

    # Calculate the difference in cost between Monica and Lewis's street
    difference = LEWIS_LENGTH - MONICA_LENGTH

    # Calculate the total cost
    total_cost = difference * COST_PER_METER

    # Display the total cost
    result = total_cost
    return result

print(solution())