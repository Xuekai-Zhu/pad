def solution():
    
    blocks_per_step = 3
    steps_per_level = 8
    total_blocks = 96
    blocks_per_level = blocks_per_step * steps_per_level
    levels = total_blocks // blocks_per_level
    result = levels
    return result

print(solution())