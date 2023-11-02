def solution():
    """For the summer, the clothing store has a 50% discount for all items. On Wednesdays, there is an additional $10.00 off on all jeans after the summer discount is applied. Before the sales tax applies, the cost of a pair of jeans is $14.50. How much was the original cost for the jeans before all the discounts?"""
    # Define the original cost of the jeans
    original_cost = 14.50

    # Apply the summer discount
    discounted_cost = original_cost * 0.5

    # Apply the Wednesday discount
    final_cost = discounted_cost - 10.0

    # Calculate the original cost before any discounts
    original_cost_before_discounts = final_cost / 0.5

    # Display the original cost
    result = original_cost_before_discounts
    return result

print(solution())