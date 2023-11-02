def solution():
    # Calculate the number of times Rosie circles the track
    # First, find how long it takes Lou to run 1 lap (0.25 miles)
    time_lap = 3 / 0.25  # Lou runs 3 miles on a track that is 0.25 miles long

    # Rosie runs at twice the speed of Lou, so it takes her half the time to run 1 lap
    time_rosie_lap = time_lap / 2

    # Calculate the number of times Rosie can complete a lap in the same time it takes Lou to complete 3 laps
    num_rosie_laps = 3 / (time_rosie_lap)

    result = num_rosie_laps
    return result

print(solution())