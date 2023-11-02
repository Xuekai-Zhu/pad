def solution():
    total_distance = 26
    num_checkpoints = 4
    distance_from_start = 1
    distance_from_finish = 1

    # Calculate the total distance covered by the checkpoints
    checkpoints_distance = total_distance - distance_from_start - distance_from_finish

    # Calculate the distance between consecutive checkpoints
    distance_between_checkpoints = checkpoints_distance / (num_checkpoints - 1)
    result = distance_between_checkpoints
    return result

print(solution())