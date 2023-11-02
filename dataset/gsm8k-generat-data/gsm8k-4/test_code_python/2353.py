def solution():
    """Bret and a team of 3 co-workers were working late so he ordered dinner for everyone. They decided on Chinese. Each main meal costs $12.0. They also ordered 2 appetizers that were $6.00 each. He includes a 20% tip and an extra $5.00 to make it a rush order. How much does Bret spend on dinner?"""
    # Define the cost of each main meal and the number of people
    MAIN_MEAL_COST = 12.0
    NUM_PEOPLE = 4

    # Define the cost of the appetizers
    APPETIZER_COST = 6.0 * 2

    # Calculate the subtotal
    subtotal = (MAIN_MEAL_COST * NUM_PEOPLE) + APPETIZER_COST

    # Calculate the cost of the tip
    tip = subtotal * 0.2

    # Add the rush cost
    total_cost = subtotal + tip + 5.0

    # return the result
    result = total_cost
    return result

print(solution())