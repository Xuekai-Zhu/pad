def solution():
    """Jack goes up three flights of stairs, then down six flights of stairs. If each flight of stairs has 12 steps that each each 8 inches high, how many feet further down is Jack than when he started?"""
    # Define the height of each step in feet
    STEP_HEIGHT = 8 / 12

    # Define the number of steps in each flight
    STEPS_PER_FLIGHT = 12

    # Define the number of flights Jack goes up and down
    UP_FLIGHTS = 3
    DOWN_FLIGHTS = 6

    # Calculate the total distance Jack goes up in feet
    up_distance = STEP_HEIGHT * STEPS_PER_FLIGHT * UP_FLIGHTS

    # Calculate the total distance Jack goes down in feet
    down_distance = STEP_HEIGHT * STEPS_PER_FLIGHT * DOWN_FLIGHTS

    # Calculate the net distance Jack goes down in feet
    net_distance = down_distance - up_distance

    result = net_distance
    return result

print(solution())