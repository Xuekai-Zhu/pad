def solution():
    """Jack goes up three flights of stairs, then down six flights of stairs. If each flight of stairs has 12 steps that each each 8 inches high, how many feet further down is Jack than when he started?"""
    # Define the number of steps per flight and the height of each step in inches
    STEPS_PER_FLIGHT = 12
    STEP_HEIGHT_INCHES = 8

    # Calculate the total vertical distance Jack traveled up and down in inches
    vertical_distance = (3 * STEPS_PER_FLIGHT * STEP_HEIGHT_INCHES) - (6 * STEPS_PER_FLIGHT * STEP_HEIGHT_INCHES)

    # Convert the vertical distance to feet
    vertical_distance_feet = vertical_distance / 12

    # Display how many feet further down Jack traveled
    result = vertical_distance_feet
    return result

print(solution())