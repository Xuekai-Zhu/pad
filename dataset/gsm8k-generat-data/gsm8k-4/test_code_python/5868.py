def solution():
    """Jessie's community built a new hedge. Each section of the hedge used 30 pieces of concrete blocks that cost $2 per piece. The hedge has eight sections. How much did they spend on the concrete blocks?"""
    # Define the cost per concrete block and the number of blocks per section
    COST_PER_BLOCK = 2
    BLOCKS_PER_SECTION = 30

    # Calculate the total cost of the concrete blocks for all sections of the hedge
    total_cost = COST_PER_BLOCK * BLOCKS_PER_SECTION * 8

    # return the result
    result = total_cost
    return result

print(solution())