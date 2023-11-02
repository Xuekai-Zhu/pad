def solution():
    rotations_per_block = 200
    current_rotations = 600
    blocks_left = 8
    
    # Calculate the total rotations needed to complete the blocks
    total_rotations = (blocks_left * rotations_per_block) - current_rotations
    result = total_rotations
    return result

print(solution())