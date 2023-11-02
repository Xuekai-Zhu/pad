def solution():
    """Jude bought three chairs for his house, all at the same price. He also bought a table that costs $50 and two sets of plates at $20 for each set. After giving the cashier $130, Jude got a $4 change. How much did each of the chairs cost?"""
    # Define the total amount spent by Jude
    total_spent = 130 - 4

    # Calculate the total cost of the table and plates
    table_cost = 50
    plates_cost = 20 * 2
    total_misc_cost = table_cost + plates_cost

    # Calculate the cost of the chairs
    chairs_cost = (total_spent - total_misc_cost) / 3

    result = chairs_cost
    return result

print(solution())