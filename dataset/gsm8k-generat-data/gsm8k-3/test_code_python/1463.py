def solution():
    """Ned is an explosives specialist racing to deactivate a time bomb on the top floor of a building. The building has twenty flights of stairs to the top floor, and Ned can run up one flight of stairs in eleven seconds. The time bomb has 72 seconds left on the timer, and Ned has spent 165 seconds running up the stairs. How many seconds will Ned have to diffuse the bomb when he reaches it?"""

    # Define the number of flights of stairs and time it takes Ned to run up one flight
    flights = 20
    time_per_flight = 11

    # Calculate the total time Ned spends running up the stairs
    total_time_running = flights * time_per_flight

    # Calculate the time Ned will have left to diffuse the bomb
    time_left = 72 - (165 - total_time_running)

    # Display the time Ned will have to diffuse the bomb
    result = time_left
    return result

print(solution())