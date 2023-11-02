def solution():
    table_cost = 140
    chair_cost_ratio = 1/7
    num_chairs = 4

    # Calculate the cost of one chair
    chair_cost = table_cost * chair_cost_ratio

    # Calculate the total cost of four chairs
    total_chair_cost = num_chairs * chair_cost

    # Calculate the total cost of one table and four chairs
    total_cost = table_cost + total_chair_cost
    result = total_cost
    return result

print(solution())