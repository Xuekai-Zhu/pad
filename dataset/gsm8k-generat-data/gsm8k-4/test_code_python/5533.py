def solution():
    """A developer was buying land. He bought 4 acres at $1,863 per acre. He then split the land he purchased into 9 lots. How much should he sell each lot for just to break even?"""
    # Define the cost of the land and the number of lots
    land_cost = 1863 * 4
    num_lots = 9

    # Calculate the total cost per lot, including the cost of the land
    lot_cost = land_cost / num_lots

    # Return the cost per lot
    result = lot_cost
    return result

print(solution())