def solution():
    """Nadine went to a garage sale and spent $56. She bought a table for $34 and 2 chairs. Each chair cost the same amount. How much did one chair cost?"""
    # Define the total amount Nadine spent and the cost of the table
    total_spent = 56
    table_cost = 34

    # Calculate the cost of the two chairs combined
    chair_cost = total_spent - table_cost

    # Divide the cost of the two chairs by two to get the cost of one chair
    one_chair_cost = chair_cost / 2

    # Display the cost of one chair
    result = one_chair_cost
    return result

print(solution())