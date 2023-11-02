def solution():
    carlos_time = 3 # minutes
    diego_distance = 0.5 # half the block
    diego_time = 2.5 # minutes

    # Calculate Diego's speed
    diego_speed = diego_distance / (diego_time/60)

    # Calculate the remaining distance for Diego
    remaining_distance = 1 - diego_distance

    # Calculate the remaining time for Diego
    remaining_time = remaining_distance / (diego_speed/60)

    # Calculate the total time for Diego
    total_time = diego_time + remaining_time

    # Calculate the average time in seconds for the racers
    average_time = ((carlos_time + total_time) / 2) * 60
    result = average_time
    return result

print(solution())