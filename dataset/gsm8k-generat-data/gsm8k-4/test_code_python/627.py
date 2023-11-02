def solution():
    """A chair costs 1/7 of the cost of a table. If a table costs $140, how much will it cost to buy a table and 4 chairs?"""
    # Define the cost of the table
    table_cost = 140

    # Define the cost of a chair as a fraction of the cost of a table
    chair_cost_fraction = 1/7

    # Calculate the cost of a chair
    chair_cost = table_cost * chair_cost_fraction

    # Calculate the total cost of buying a table and 4 chairs
    total_cost = table_cost + (4 * chair_cost)

    result = total_cost
    return result

print(solution())