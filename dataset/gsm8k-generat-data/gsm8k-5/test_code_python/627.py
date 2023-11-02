def solution():
    table_cost = 140  # A table costs $140
    chair_cost = table_cost / 7  # A chair costs 1/7 of the cost of a table
    total_cost = table_cost + (4 * chair_cost)  # The cost of a table and 4 chairs

    result = total_cost
    return result

print(solution())