def solution():
    """Nadine went to a garage sale and spent $56. She bought a table for $34 and 2 chairs. Each chair cost the same amount. How much did one chair cost?"""
    total_spent = 56
    table_cost = 34
    chairs_cost = total_spent - table_cost
    one_chair_cost = chairs_cost / 2
    result = one_chair_cost
    return result

print(solution())