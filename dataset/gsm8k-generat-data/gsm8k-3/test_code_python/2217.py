def solution():
    """Mrs. Taylor bought two smart televisions that cost $650 each. If the total sales price had a 25% discount, how much did Mrs. Taylor pay for the two televisions?"""
    # Define the original cost of one smart television
    ORIGINAL_COST = 650

    # Calculate the total cost of two smart televisions without discount
    total_cost_without_discount = ORIGINAL_COST * 2

    # Calculate the total cost of two smart televisions with 25% discount
    total_cost_with_discount = total_cost_without_discount * 0.75

    # Display the total cost with discount
    result = total_cost_with_discount
    return result

print(solution())