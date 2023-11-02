def solution():
    target_blocks = 8
    current_blocks = 3
    rotations_per_block = 200
    current_rotations = current_blocks * rotations_per_block
    remaining_rotations = target_blocks * rotations_per_block - current_rotations
    result = remaining_rotations
    return result

print(solution())