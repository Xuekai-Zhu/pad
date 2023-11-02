def solution():
    """A developer was buying land. He bought 4 acres at $1,863 per acre. He then split the land he purchased into 9 lots. How much should he sell each lot for just to break even?"""
    # Define the cost per acre
    COST_PER_ACRE = 1863

    # Define the number of acres purchased
    acres_purchased = 4

    # Define the number of lots the land was split into
    num_lots = 9

    # Calculate the total cost of the land
    total_cost = acres_purchased * COST_PER_ACRE

    # Calculate the cost per lot to break even
    cost_per_lot = total_cost / num_lots

    # Display the cost per lot
    result = cost_per_lot
    return result

print(solution())