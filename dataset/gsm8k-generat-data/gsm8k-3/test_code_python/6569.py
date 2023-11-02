def solution():
    """Ali and Leila reserve their places for a trip to Egypt. The price is $147 per person, but they were each given a discount of $14 since there are two of them. How much does their trip cost?"""
    # Define the price per person and the discount amount
    PRICE_PER_PERSON = 147
    DISCOUNT_AMOUNT = 14

    # Calculate the cost before the discount
    cost_before_discount = 2 * PRICE_PER_PERSON

    # Calculate the total discount amount
    total_discount = 2 * DISCOUNT_AMOUNT

    # Calculate the cost after the discount
    cost_after_discount = cost_before_discount - total_discount

    # Display the cost after the discount
    result = cost_after_discount
    return result

print(solution())