def solution():
    """Nadine went to a garage sale and spent $56. She bought a table for $34 and 2 chairs. Each chair cost the same amount. How much did one chair cost?"""
    total_spent = 56
    table_cost = 34
    chairs_cost = total_spent - table_cost
    num_chairs = 2
    cost_per_chair = chairs_cost / num_chairs
    result = cost_per_chair
    return result

print(solution())