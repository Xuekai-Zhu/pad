def solution():
    """Maria bought a ticket to a ZOO. The regular price stands at $15, but she was able to get a 40% discount. How much did Maria pay for the ticket?"""
    # Define the regular price and the discount percentage
    REGULAR_PRICE = 15
    DISCOUNT_PERCENTAGE = 0.4

    # Calculate the amount of the discount
    discount_amount = REGULAR_PRICE * DISCOUNT_PERCENTAGE

    # Calculate the price Maria paid after the discount
    price_after_discount = REGULAR_PRICE - discount_amount

    # return the result
    result = price_after_discount
    return result

print(solution())