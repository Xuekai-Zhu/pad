def solution():
    """Nadine went to a garage sale and spent $56. She bought a table for $34 and 2 chairs. Each chair cost the same amount. How much did one chair cost?"""
    # Define the total amount spent and the cost of the table
    total_spent = 56
    table_cost = 34
    
    # Determine the cost of the chairs
    chair_cost = (total_spent - table_cost) / 2
    
    # Return the cost of one chair
    result = chair_cost
    return result

print(solution())