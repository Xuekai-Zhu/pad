def solution():
    # Calculate the time it takes Biff to finish the race
    biff_time = 500/50

    # Calculate the distance Kenneth travels in that time
    kenneth_distance = 51 * biff_time

    # Calculate how far past the finish line Kenneth will be
    distance_past_finish = kenneth_distance - 500
    result = distance_past_finish
    return result

print(solution())