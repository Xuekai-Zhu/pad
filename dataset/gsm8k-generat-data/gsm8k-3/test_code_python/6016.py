def solution():
    """Madison and Gigi have to run a total of 2400 meters in gym class. The track is 150 meters around. If they each have run 6 laps, how many more laps do they have to run before they reach 2400 meters?"""
    # Define the length of the track in meters
    TRACK_LENGTH = 150

    # Define the number of laps already run
    laps_run = 6

    # Calculate the total distance already run
    distance_run = laps_run * TRACK_LENGTH

    # Calculate the distance left to run
    distance_left = 2400 - distance_run

    # Calculate the number of laps left to run
    laps_left = distance_left // TRACK_LENGTH

    # Display the number of laps left to run
    result = laps_left
    return result

print(solution())