def solution():
    # Define the cost of the table
    table_cost = 140

    # Define the cost of one chair
    chair_cost = table_cost / 7

    # Calculate the total cost of 4 chairs
    chairs_total_cost = 4 * chair_cost

    # Calculate the total cost of a table and 4 chairs
    total_cost = table_cost + chairs_total_cost
    result = total_cost
    return result

print(solution())