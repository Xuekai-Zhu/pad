def solution():
    """Austin and Jake start descending from the 9th floor of a building at the same time. Austin uses the elevator and Jake uses the stairs, descending 3 steps every second. The stairs have 30 steps across each floor. If the elevator will take a minute to get to ground level, how many seconds later will Jake get to the ground floor?"""
    # Define the number of floors in the building
    NUM_FLOORS = 9

    # Define the number of steps per floor
    STEPS_PER_FLOOR = 30

    # Define the time it takes for the elevator to reach ground level in seconds
    ELEVATOR_TIME = 60

    # Calculate the total number of steps Jake must descend
    total_steps = NUM_FLOORS * STEPS_PER_FLOOR

    # Calculate the time it will take Jake to descend all the steps in seconds
    jake_time = total_steps / 3

    # Calculate the time difference between Jake and Austin in seconds
    time_difference = jake_time - ELEVATOR_TIME

    # Display the time difference
    result = time_difference
    return result

print(solution())