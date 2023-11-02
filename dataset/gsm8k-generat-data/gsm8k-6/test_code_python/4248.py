def solution():
    # Calculate the total distance Albert has already run
    distance_covered = 6 * 9

    # Calculate the remaining distance he needs to cover
    remaining_distance = 99 - distance_covered

    # Calculate the complete laps Albert will make around the track
    complete_laps = remaining_distance // 9

    result = complete_laps
    return result

print(solution())