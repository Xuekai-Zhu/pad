def solution():
    """Albert has to run 99 meters in gym class. The track is 9 meters around. He has already run 6 times around it. Once he finishes, how many more complete laps will he have made around the track?"""
    # Define the total distance and distance already covered
    total_distance = 99
    distance_covered = 6*9

    # Calculate the distance remaining
    distance_remaining = total_distance - distance_covered

    # Calculate the number of complete laps remaining
    laps_remaining = distance_remaining // 9

    # Return the result
    result = laps_remaining
    return result

print(solution())