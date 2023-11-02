def solution():
    # Calculate the total distance between the checkpoints (excluding the first and last checkpoint)
    total_distance = 26 - 2

    # Calculate the number of checkpoints (excluding the first and last checkpoint)
    num_checkpoints = 4 - 2

    # Calculate the distance between each consecutive checkpoint
    distance_between_checkpoints = total_distance / num_checkpoints
    result = distance_between_checkpoints
    return result

print(solution())