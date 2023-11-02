def solution():
    total_distance = 26  # The marathon is 26 miles in total
    num_checkpoints = 4  # There are 4 checkpoints
    checkpoints_distance = (total_distance - 2) / num_checkpoints  # Subtract the start and finish line distance from the total and divide equally between checkpoints
    result = checkpoints_distance
    return result

print(solution())