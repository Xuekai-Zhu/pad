def solution():
    """Hannah brought $30 to the county fair. She spent half of it on rides and another $5 on dessert. How much, in dollars, is left?"""
    # Define the initial amount Hannah brought
    initial_amount = 30

    # Calculate the amount spent on rides
    rides_spending = initial_amount / 2

    # Calculate the total amount spent
    total_spending = rides_spending + 5

    # Calculate the amount left
    amount_left = initial_amount - total_spending

    # Display the amount left
    result = amount_left
    return result

print(solution())