def solution():
    initial_distance = 100
    initial_time = 1
    remaining_distance = 300
    speed = remaining_distance / (initial_time + 1) # Average speed for remaining distance
    total_time = initial_time + (remaining_distance / speed) # Total time for the whole journey
    result = total_time
    return result

print(solution())