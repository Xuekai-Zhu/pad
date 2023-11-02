def solution():
    total_distance = 99  # Albert has to run 99 meters
    track_distance = 9  # Each lap around the track is 9 meters
    completed_laps = 6  # Albert has already run 6 complete laps

    # Calculate the remaining distance that Albert has to run
    remaining_distance = total_distance - (track_distance * completed_laps)

    # Calculate the number of complete laps Albert will run after he finishes
    complete_laps_remaining = remaining_distance // track_distance
    result = complete_laps_remaining
    return result

print(solution())