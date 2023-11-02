def solution():
    """Tom uses 10 weight plates each weighing 30 pounds on an exercise machine.  This exercise machine uses special technology to make the weights 20% heavier on the lowering portion.  How heavy did the weights feel when being lowered?"""
    # Define the weight of each plate
    weight_plate = 30

    # Define the number of plates
    num_plates = 10

    # Calculate the total weight of the plates
    total_weight = weight_plate * num_plates

    # Calculate the weight increase
    weight_increase = total_weight * 0.2

    # Calculate the weight of the plates when being lowered
    lowered_weight = total_weight + weight_increase

    # Display the weight of the plates when being lowered
    result = lowered_weight
    return result

print(solution())