def solution():
    time_waiting = 2  # Martin spends 2 hours waiting in traffic
    time_getting_off = 4 * time_waiting  # Martin spends 4 times the waiting time trying to get off the freeway

    # Calculate the total time wasted
    total_time_wasted = time_waiting + time_getting_off
    result = total_time_wasted
    return result

print(solution())