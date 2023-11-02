def solution():
    # Find the cost of one chair
    cost_of_chair = (1/7) * 140  # 1/7 of the cost of a table, which is $140

    # Calculate the total cost of buying a table and 4 chairs
    total_cost = 140 + 4 * cost_of_chair
    result = total_cost
    return result

print(solution())