def solution():
    total_cost = 135
    table_cost = 55
    num_chairs = 4

    # Calculate the total cost of all chairs
    total_chair_cost = total_cost - table_cost

    # Calculate the cost of one chair
    chair_cost = total_chair_cost / num_chairs
    result = chair_cost
    return result

print(solution())