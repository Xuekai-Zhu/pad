def solution():
    """Ned is an explosives specialist racing to deactivate a time bomb on the top floor of a building.
    The building has twenty flights of stairs to the top floor, and Ned can run up one flight of stairs in
    eleven seconds. The time bomb has 72 seconds left on the timer, and Ned has spent 165 seconds running up
    the stairs. How many seconds will Ned have to diffuse the bomb when he reaches it?"""
    # Define the number of flights of stairs
    num_stairs = 20

    # Define the time it takes to run up one flight of stairs
    time_per_stair = 11

    # Calculate the total time it takes to run up all the stairs
    total_stair_time = num_stairs * time_per_stair

    # Calculate the time Ned has left to diffuse the bomb
    time_left = 72 - (165 + total_stair_time)

    # return the result
    result = time_left
    return result

print(solution())