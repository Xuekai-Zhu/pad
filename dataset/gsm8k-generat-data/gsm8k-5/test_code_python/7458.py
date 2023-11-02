def solution():
    distance_per_lap = 0.25  # The track is a one-quarter mile circular track
    laps_completed_by_polly = 12  # Polly managed to circle the track 12 times
    time_taken_by_polly = 0.5  # Polly completed the laps in one half hour

    # Calculate the total distance covered by Polly
    total_distance_covered_by_polly = distance_per_lap * laps_completed_by_polly

    # Calculate Polly's speed in miles per hour
    speed_of_polly = total_distance_covered_by_polly / time_taken_by_polly

    # Calculate the speed of Gerald's car
    speed_of_gerald = speed_of_polly / 2

    result = speed_of_gerald
    return result

print(solution())