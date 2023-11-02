def solution():
    blocks_per_step = 3  # Each step has 3 blocks of stone
    steps_per_level = 8  # Each level has 8 steps
    total_blocks = 96  # Clara climbed past 96 blocks of stone

    # Calculate the total number of steps Clara climbed
    total_steps = total_blocks / blocks_per_step

    # Calculate the number of levels the tower has
    num_levels = total_steps / steps_per_level
    result = num_levels
    return result

print(solution())