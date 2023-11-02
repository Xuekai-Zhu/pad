def solution():
    
    blocks_to_ride = 8
    rotations_per_block = 200
    starting_rotations = 600
    total_rotations_needed = blocks_to_ride * rotations_per_block
    rotations_remaining = total_rotations_needed - starting_rotations
    result = rotations_remaining
    return result

print(solution())