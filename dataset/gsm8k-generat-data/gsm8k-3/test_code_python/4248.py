def solution():
    """Albert has to run 99 meters in gym class. The track is 9 meters around. He has already run 6 times around it. Once he finishes, how many more complete laps will he have made around the track?"""
    # Define the distance of the track
    TRACK_DISTANCE = 9

    # Calculate the distance Albert has already run
    distance_run = 6 * TRACK_DISTANCE

    # Calculate the distance Albert still needs to run
    distance_left = 99 - distance_run

    # Calculate the number of complete laps Albert will make around the track
    laps_completed = distance_left // TRACK_DISTANCE

    # Display the number of laps completed
    result = laps_completed
    return result

print(solution())