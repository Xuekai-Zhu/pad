def solution():
    # Define the cost and quantity of each concrete block
    cost_per_block = 2
    blocks_per_section = 30

    # Calculate the total cost of the concrete blocks for all eight sections
    total_blocks = blocks_per_section * 8
    total_cost = total_blocks * cost_per_block

    result = total_cost
    return result

print(solution())