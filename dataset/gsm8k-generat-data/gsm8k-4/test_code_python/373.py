def solution():
    """Alison bought some storage tubs for her garage. She bought 3 large ones and 6 small ones, for $48 total. If the large tubs cost $6, how much do the small ones cost?"""
    # Define the cost of a large tub
    large_tub_cost = 6

    # Define the number of large tubs
    num_large_tubs = 3

    # Define the total number of tubs
    total_tubs = num_large_tubs + 6

    # Calculate the total cost of the tubs
    total_cost = 48

    # Calculate the cost of the small tubs
    small_tub_cost = (total_cost - (num_large_tubs * large_tub_cost)) / 6

    result = small_tub_cost
    return result

print(solution())