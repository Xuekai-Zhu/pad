def solution():
    blocks_to_ride = 8  # Greg wants to ride at least 8 blocks
    rotations_per_block = 200  # Greg's wheels rotate 200 times per block
    initial_rotations = 600  # Greg's wheels have already rotated 600 times

    # Calculate the total number of rotations required to reach Greg's goal
    total_rotations = blocks_to_ride * rotations_per_block
    remaining_rotations = total_rotations - initial_rotations
    result = remaining_rotations
    return result

print(solution())