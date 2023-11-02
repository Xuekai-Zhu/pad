def solution():
    """Jason's stove catches on fire. Buying a replacement will cost $1200 and fixing the damage to the wall behind it will cost 1/6th as much. How much does he spend in total?"""
    # Define the cost of the new stove
    stove_cost = 1200

    # Define the cost of repairing the wall
    wall_repair_cost = stove_cost / 6

    # Calculate the total cost
    total_cost = stove_cost + wall_repair_cost

    # Return the result
    result = total_cost
    return result

print(solution())