def solution():
    """Tobias went to a swimming pool for 3 hours. Swimming every 100 meters took him 5 minutes, but every 25 minutes he had to take a 5-minute pause. How many meters did Tobias swim during his visit to the swimming pool?"""
    # Define Tobias' swimming speed
    SPEED = 100 / 5  # meters per minute

    # Define the swimming and pause time in minutes
    SWIMMING_TIME = 5
    PAUSE_TIME = 5

    # Define the total pool time in minutes
    TOTAL_TIME = 3 * 60  # 3 hours to minutes

    # Initialize the distance and time traveled
    distance = 0
    time = 0

    # Continue swimming until the total time has been reached
    while time < TOTAL_TIME:
        # Add the distance traveled during the swimming time
        distance += SPEED * SWIMMING_TIME

        # Add the time spent swimming and taking a pause
        time += SWIMMING_TIME + PAUSE_TIME

        # Take a longer pause every 25 minutes
        if time % 25 == 0:
            time += PAUSE_TIME

    # Return the distance traveled
    result = distance
    return result

print(solution())