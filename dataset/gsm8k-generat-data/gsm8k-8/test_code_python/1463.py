def solution():
    # Calculate the total time spent running up the stairs
    total_time_running = 165

    # Calculate the time remaining on the timer when Ned starts running
    time_remaining = 72

    # Calculate how many flights of stairs Ned has run up
    flights_of_stairs = total_time_running // 11

    # Calculate how many seconds Ned has left to diffuse the bomb
    seconds_left = time_remaining - total_time_running - (flights_of_stairs * 11)

    result = seconds_left
    return result

print(solution())