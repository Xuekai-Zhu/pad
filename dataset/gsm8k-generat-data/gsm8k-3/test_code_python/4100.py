def solution():
    """A 26-mile circular marathon has four checkpoints inside it. The first is one mile from the start line, and the last checkpoint is one mile from the finish line. The checkpoints have equal spacing between them. How many miles apart are each of the consecutive checkpoints between the start-finish line?"""
    # Define the total distance of the marathon
    distance = 26

    # Define the distance of the checkpoints from the start line and finish line
    checkpoint_distance = 1

    # Calculate the total distance between the checkpoints
    total_checkpoint_distance = distance - 2*checkpoint_distance
    
    # Divide the total distance between the checkpoints by the number of checkpoints
    num_checkpoints = 4
    checkpoint_spacing = total_checkpoint_distance / (num_checkpoints - 1)

    # Display the distance between each consecutive checkpoint
    result = checkpoint_spacing
    return result

print(solution())