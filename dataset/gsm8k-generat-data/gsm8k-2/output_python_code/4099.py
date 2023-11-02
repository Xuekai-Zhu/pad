def solution():
    """A 26-mile circular marathon has four checkpoints inside it. The first is one mile from the start line, and the last checkpoint is one mile from the finish line. The checkpoints have equal spacing between them. How many miles apart are each of the consecutive checkpoints between the start-finish line?"""
    total_distance = 26
    num_checkpoints = 4
    checkpoint_distance = (total_distance - 2) / num_checkpoints
    result = checkpoint_distance
    return result

print(solution())