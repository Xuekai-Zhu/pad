def solution():
    
    # Define the cost of a regular box of dishwasher pods and the increase percentage
    REGULAR_BOX_PRICE = 12
    INCREASE_PERCENTAGE = 20

    # Calculate the number of dishwasher pods in the size box
    size_boxes_pods = REGULAR_BOX_PRICE * (1 + INCREASE_PERCENTAGE / 100)

    # Calculate the number of dishwasher cycles the new box can run for $1
    dishwashing_cycles = size_boxes_pods // 1

    # Display the number of dishwashing cycles the new box can run for $1
    result = dishwashing_cycles
    return result

print(solution())