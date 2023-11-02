def solution():
    time_per_lawn = 30/60  # convert 30 minutes to hours
    num_yards = 8
    num_days = 2

    # Calculate the total time spent cutting grass
    total_time = time_per_lawn * num_yards * num_days
    
    result = total_time
    return result

print(solution())