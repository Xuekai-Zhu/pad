def solution():
    """A chair costs 1/7 of the cost of a table. If a table costs $140, how much will it cost to buy a table and 4 chairs?"""
    table_cost = 140
    chair_cost = table_cost / 7
    total_cost = table_cost + (4 * chair_cost)
    result = total_cost
    return result

print(solution())