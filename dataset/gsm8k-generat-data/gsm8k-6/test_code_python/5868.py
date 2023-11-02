def solution():
    # Calculate the total cost of the concrete blocks for the hedge
    cost_per_block = 2
    blocks_per_section = 30
    total_sections = 8
    total_blocks = blocks_per_section * total_sections
    total_cost = total_blocks * cost_per_block
    result = total_cost
    return result

print(solution())