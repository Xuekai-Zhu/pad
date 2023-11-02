def solution():
    steps_per_level = 8
    blocks_per_step = 3
    total_blocks = 96
    levels = total_blocks / (steps_per_level * blocks_per_step)
    result = levels
    return result

print(solution())