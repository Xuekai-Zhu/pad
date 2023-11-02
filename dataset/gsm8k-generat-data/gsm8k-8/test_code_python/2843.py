def solution():
    # Define the number of rotations per block
    rotations_per_block = 200

    # Define the number of blocks remaining
    blocks_remaining = 8

    # Define the current number of rotations
    current_rotations = 600

    # Calculate the total number of rotations needed to reach the goal
    total_rotations_needed = rotations_per_block * blocks_remaining

    # Calculate the number of rotations needed to reach the goal from the current point
    rotations_needed = total_rotations_needed - current_rotations
    result = rotations_needed
    return result

print(solution())