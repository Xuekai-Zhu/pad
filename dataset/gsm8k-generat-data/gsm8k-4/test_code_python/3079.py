def solution():
    """For the summer, the clothing store has a 50% discount for all items. On Wednesdays, there is an additional $10.00 off on all jeans after the summer discount is applied. Before the sales tax applies, the cost of a pair of jeans is $14.50. How much was the original cost for the jeans before all the discounts?"""
    # Define the cost of the jeans before any discount
    original_cost = None

    # Define the final cost of the jeans after all the discounts
    final_cost = 14.50

    # Apply 50% discount for the summer sale
    final_cost -= final_cost * 0.5

    # Apply additional $10 discount for Wednesday's sale
    final_cost -= 10

    # Calculate the original cost of the jeans before all the discounts
    original_cost = final_cost / 0.5

    # Return the result
    result = round(original_cost, 2)
    return result

print(solution())