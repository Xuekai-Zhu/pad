def solution():
    # Convert all time to hours for consistency
    time1 = 0.5  # half an hour
    time2 = 0.5  # half an hour
    time3 = 0.25  # 15 minutes

    # Calculate the distance of each segment of the run
    distance1 = 10 * time1
    distance2 = 20 * time2
    distance3 = 8 * time3

    # Calculate the total distance
    total_distance = distance1 + distance2 + distance3
    result = total_distance
    return result

print(solution())