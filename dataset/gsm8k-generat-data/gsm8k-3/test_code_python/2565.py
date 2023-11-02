def solution():
    """John climbs up 9 flights of stairs. Each flight is 10 feet. If each step is 18 inches, how many steps does he climb up?"""
    # Define the height of each flight in inches
    FLIGHT_HEIGHT = 10 * 12

    # Define the height of each step in inches
    STEP_HEIGHT = 18

    # Calculate the number of steps climbed up
    total_steps = (FLIGHT_HEIGHT * 9) / STEP_HEIGHT

    result = total_steps
    return result

print(solution())