def solution():
    """Jason's stove catches on fire. Buying a replacement will cost $1200 and fixing the damage to the wall behind it will cost 1/6th as much. How much does he spend in total?"""
    # Define the cost of a replacement stove
    STOVE_COST = 1200

    # Calculate the cost of fixing the wall
    WALL_COST = STOVE_COST / 6

    # Calculate the total cost
    total_cost = STOVE_COST + WALL_COST

    # Display the total cost
    result = total_cost
    return result

print(solution())