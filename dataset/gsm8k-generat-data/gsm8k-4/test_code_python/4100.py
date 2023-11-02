def solution():
    """A 26-mile circular marathon has four checkpoints inside it.The first is one mile from the start line, and the last checkpoint is one mile from the finish line. The checkpoints have equal spacing between them. How many miles apart are each of the consecutive checkpoints between the start-finish line?"""
    # Define the total length of the marathon
    marathon_length = 26

    # Define the distance between the first checkpoint and the start and the last checkpoint and the finish
    start_checkpoint = 1
    finish_checkpoint = 1

    # Define the number of checkpoints in between the first and the last
    num_checkpoints = 4

    # Calculate the total distance between the start and finish checkpoints
    total_distance = marathon_length - start_checkpoint - finish_checkpoint

    # Calculate the distance between each consecutive checkpoint
    checkpoint_distance = total_distance / num_checkpoints

    # return the result
    result = checkpoint_distance
    return result

print(solution())