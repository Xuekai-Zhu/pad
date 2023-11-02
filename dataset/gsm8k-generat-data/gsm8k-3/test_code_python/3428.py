def solution():
    """Jorge bought 24 tickets for $7 each. For purchasing so many, he is given a discount of 50%. How much, in dollars, did he spend on tickets?"""
    # Define the original ticket price and the discount
    ORIGINAL_PRICE = 7
    DISCOUNT_PERCENTAGE = 50

    # Calculate the total cost without the discount
    total_cost = 24 * ORIGINAL_PRICE

    # Calculate the amount of the discount
    discount_amount = total_cost * (DISCOUNT_PERCENTAGE / 100)

    # Calculate the final cost with the discount
    final_cost = total_cost - discount_amount

    # Display the final cost
    result = final_cost
    return result

print(solution())