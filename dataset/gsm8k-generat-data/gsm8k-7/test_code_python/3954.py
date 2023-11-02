def solution():
    starting_blocks = 0
    building_blocks = 80
    farmhouse_blocks = 123
    fenced_blocks = 57
    left_blocks = 84

    # Calculate the total number of blocks used
    total_blocks_used = building_blocks + farmhouse_blocks + fenced_blocks

    # Calculate the starting number of blocks
    starting_blocks = total_blocks_used + left_blocks
    result = starting_blocks
    return result

print(solution())