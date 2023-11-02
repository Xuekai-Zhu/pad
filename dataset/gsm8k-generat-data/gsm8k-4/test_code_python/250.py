def solution():
    """Tom uses 10 weight plates each weighing 30 pounds on an exercise machine. This exercise machine uses special technology to make the weights 20% heavier on the lowering portion. How heavy did the weights feel when being lowered?"""
    # Define the weight of each plate
    plate_weight = 30

    # Calculate the additional weight added during the lowering portion
    additional_weight = plate_weight * 0.2

    # Calculate the total weight of each plate during the lowering portion
    total_weight = plate_weight + additional_weight

    # Calculate the total weight of all 10 plates during the lowering portion
    total_lowering_weight = total_weight * 10

    result = total_lowering_weight
    return result

print(solution())