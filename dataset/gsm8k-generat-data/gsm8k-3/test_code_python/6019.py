def solution():
    """Mark buys a Magic card for $100, which then triples in value.  How much profit would he make selling it?"""
    # Define the initial cost and the new value
    initial_cost = 100
    new_value = initial_cost * 3

    # Calculate the profit
    profit = new_value - initial_cost

    # Display the profit
    result = profit
    return result

print(solution())