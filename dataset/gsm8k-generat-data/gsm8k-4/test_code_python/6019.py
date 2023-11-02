def solution():
    """Mark buys a Magic card for $100, which then triples in value.  How much profit would he make selling it?"""
    # Define the initial cost and the increased value of the Magic card
    initial_cost = 100
    increased_value = 3 * initial_cost

    # Calculate the profit made by selling the Magic card
    profit = increased_value - initial_cost
    
    result = profit
    return result

print(solution())