def solution():
    
    # Define the number of boxes and fireworks per box
    BOXES_PER_STREET = 15
    BOXES_PER_FIREWORK = 20

    # Calculate the total number of fireworks
    total_fireworks = (BOXES_PER_STREET * BOXES_PER_FIREWORK) + (3 * BOXES_PER_FIREWORK) + (5 * BOXES_PER_STREET)

    # Display the total number of fireworks
    result = total_fireworks
    return result

print(solution())