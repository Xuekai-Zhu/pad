def solution():
    total_spent = 56  # Nadine spent $56 in total
    table_cost = 34  # Nadine spent $34 on a table
    remaining_cost = total_spent - table_cost  # The remaining cost is the cost of the chairs
    num_chairs = 2  # Nadine bought 2 chairs

    # Calculate the cost of each chair
    chair_cost = remaining_cost / num_chairs
    result = chair_cost
    return result

print(solution())