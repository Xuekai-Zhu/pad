def solution():
    # Define the total amount spent and the cost of the table
    total_spent = 56
    table_cost = 34

    # Calculate the cost of the two chairs combined
    chair_cost_combined = total_spent - table_cost

    # Divide the cost of the chairs by 2 to get the cost of one chair
    one_chair_cost = chair_cost_combined / 2
    result = one_chair_cost
    return result

print(solution())