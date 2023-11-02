def solution():
    """A chair costs 1/7 of the cost of a table. If a table costs $140, how much will it cost to buy a table and 4 chairs?"""
    # Define the cost of a table and the ratio of chair cost to table cost
    TABLE_COST = 140
    CHAIR_RATIO = 1/7

    # Calculate the cost of a chair
    chair_cost = CHAIR_RATIO * TABLE_COST

    # Calculate the total cost of a table and 4 chairs
    total_cost = TABLE_COST + (4 * chair_cost)

    # Display the total cost
    result = total_cost
    return result

print(solution())