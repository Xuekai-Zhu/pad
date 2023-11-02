def solution():
    """Jessie's community built a new hedge. Each section of the hedge used 30 pieces of concrete blocks that cost $2 per piece. The hedge has eight sections. How much did they spend on the concrete blocks?"""
    # Define the cost per piece of concrete block and the number of sections in the hedge
    COST_PER_PIECE = 2
    NUM_SECTIONS = 8

    # Calculate the total number of concrete blocks needed
    total_blocks = NUM_SECTIONS * 30

    # Calculate the total cost of the concrete blocks
    total_cost = total_blocks * COST_PER_PIECE

    # Display the total cost
    result = total_cost
    return result

print(solution())