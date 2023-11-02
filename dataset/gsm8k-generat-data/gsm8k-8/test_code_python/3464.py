def solution():
    # Define Lisa's walking speed and time
    speed = 10 # meters per minute
    time = 60 # minutes per day

    # Calculate Lisa's total walking distance in one day
    distance_per_day = speed * time

    # Calculate Lisa's total walking distance in two days
    total_distance = distance_per_day * 2
    result = total_distance
    return result

print(solution())