def solution():
    # Calculate the total number of steps climbed
    total_blocks = 96
    total_steps = total_blocks / 3  # each step is made up of 3 blocks
    total_levels = total_steps / 8  # each level has 8 steps
    result = total_levels
    return result

print(solution())