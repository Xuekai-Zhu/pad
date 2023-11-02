def solution():
    distance_to_market = 30  # Greg drives 30 miles from his workplace to the farmers market
    time_to_drive_home = 0.5  # Greg drives for 30 minutes, which is half an hour
    speed_to_drive_home = 20  # Greg drives at a speed of 20 miles per hour to get home

    # Calculate the distance Greg travels to get home
    distance_to_home = time_to_drive_home * speed_to_drive_home

    # Calculate the total distance Greg travels
    total_distance = distance_to_market + distance_to_home
    result = total_distance
    return result

print(solution())