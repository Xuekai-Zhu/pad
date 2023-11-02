def solution():
    total_spent = 56
    table_cost = 34
    num_chairs = 2

    # Calculate the total cost of the chairs
    chairs_cost = total_spent - table_cost

    # Calculate the cost of one chair
    cost_per_chair = chairs_cost / num_chairs
    result = cost_per_chair
    return result

print(solution())