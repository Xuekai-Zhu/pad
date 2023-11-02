def solution():
    # Calculate the total time it takes to get to the school building
    total_travel_time = 15 + 6  # 15 minutes to arrive at the school gate and 6 minutes to get to the school building
    # Calculate the time left to get to the room without being late
    time_left = 30 - total_travel_time
    result = time_left
    return result

print(solution())