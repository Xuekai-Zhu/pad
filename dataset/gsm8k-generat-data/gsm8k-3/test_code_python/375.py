def solution():
    """Alison bought some storage tubs for her garage. She bought 3 large ones and 6 small ones, for $48 total. If the large tubs cost $6, how much do the small ones cost?"""
    # Define the cost of a large tub
    LARGE_TUB_COST = 6

    # Define the number of large and small tubs purchased
    large_tubs = 3
    small_tubs = 6

    # Calculate the total cost of the large tubs
    large_tub_cost = large_tubs * LARGE_TUB_COST

    # Calculate the cost of the small tubs
    small_tub_cost = 48 - large_tub_cost

    # Calculate the cost of each small tub
    cost_per_small_tub = small_tub_cost / small_tubs

    # Display the cost per small tub
    result = cost_per_small_tub
    return result

print(solution())