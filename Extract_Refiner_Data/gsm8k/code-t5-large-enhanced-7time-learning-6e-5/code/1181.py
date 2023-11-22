def solution():
    
    # Define the number of slices per pizza
    CHEESE_SLICES = 12
    PEPPERONI_SLICES = 8

    # Define the number of friends
    num_friends = 6

    # Calculate the total number of slices eaten
    total_slices = (6 * CHEESE_SLICES) + (4 * PEPPERONI_SLICES)

    # Calculate the number of pizza pies needed
    pies_needed = total_slices // CHEESE_SLICES + (total_slices % PEPPERONI_SLICES > 0)

    # Display the number of pizza pies needed
    result = pies_needed
    return result

print(solution())