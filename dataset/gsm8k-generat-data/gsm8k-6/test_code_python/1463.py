def solution():
    # Calculate the total time Ned spends on the stairs
    total_stairs_time = 20 * 11  # Ned can run up one flight of stairs in 11 seconds and there are 20 flights

    # Calculate the time Ned has left to defuse the bomb
    time_left = 72 - (165 - total_stairs_time)  # subtract the time spent on stairs from the total time Ned has to defuse the bomb
    result = time_left
    return result

print(solution())