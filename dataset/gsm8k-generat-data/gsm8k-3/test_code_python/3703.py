def solution():
    """Jason is planning a parking garage that will have 12 floors. Every 3rd floor has a gate where drivers have to show ID, which takes two minutes. To get from one floor to the next, drivers have to drive 800 feet at 10 feet/second. How long, in seconds, does it take to get to the bottom of the garage from the top?"""
    # Define the number of floors and the distance between floors
    NUM_FLOORS = 12
    DISTANCE_BETWEEN_FLOORS = 800

    # Define the time it takes to show ID at a gate
    ID_TIME = 2 * 60  # in seconds

    # Calculate the total time to get from the top floor to the bottom floor
    total_time = 0
    for floor in range(NUM_FLOORS, 0, -1):
        # Add the time to drive between floors
        total_time += DISTANCE_BETWEEN_FLOORS / 10  # distance/speed

        # If this is a 3rd floor (or every 3 floors), add the time to show ID at the gate
        if floor % 3 == 0:
            total_time += ID_TIME

    # Display the total time in seconds
    result = total_time
    return result

print(solution())