def solution():
    
    rotations_per_block = 200
    blocks_to_ride = 8
    starting_rotations = 600
    total_rotations_needed = (blocks_to_ride * rotations_per_block) - starting_rotations
    result = total_rotations_needed
    return result

print(solution())