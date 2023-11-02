def solution():
    total_track_length = 9
    distance_left = 99 - (total_track_length * 6)

    # Calculate how many complete laps Albert will make once he finishes
    complete_laps = distance_left // total_track_length

    result = complete_laps
    return result

print(solution())