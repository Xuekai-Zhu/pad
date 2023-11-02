def solution():
    blocks_per_section = 30
    cost_per_block = 2
    num_sections = 8

    # Calculate the total number of blocks needed for the entire hedge
    total_blocks = blocks_per_section * num_sections

    # Calculate the total cost of all the blocks
    total_cost = total_blocks * cost_per_block
    result = total_cost
    return result

print(solution())