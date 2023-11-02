def solution():
    """Bret and a team of 3 co-workers were working late so he ordered dinner for everyone.  They decided on Chinese.  Each main meal costs $12.0.  They also ordered 2 appetizers that were $6.00 each.  He includes a 20% tip and an extra $5.00 to make it a rush order.  How much does Bret spend on dinner?"""
    # Define the cost of each dinner and appetizer
    MAIN_MEAL_COST = 12.0
    APPETIZER_COST = 6.0

    # Define the number of dinners and appetizers ordered
    num_dinners = 4
    num_appetizers = 2

    # Calculate the total cost of the dinners
    dinner_cost = num_dinners * MAIN_MEAL_COST

    # Calculate the total cost of the appetizers
    appetizer_cost = num_appetizers * APPETIZER_COST

    # Calculate the total cost including tip and rush order fee
    total_cost = (dinner_cost + appetizer_cost) * 1.2 + 5.0

    # Display the total cost
    result = total_cost
    return result

print(solution())