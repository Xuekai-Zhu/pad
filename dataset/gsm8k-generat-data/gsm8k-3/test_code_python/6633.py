def solution():
    """Dennis wants to buy 4 pairs of pants from the store which cost $110.00 each with a 30% discount and he also wants to buy 2 pairs of socks which cost $60.00 with a 30% discount. How much money will Dennis have to spend in total after he bought all the items he wants after the discount?"""
    # Define the original prices of the pants and socks
    PANTS_PRICE = 110
    SOCKS_PRICE = 60

    # Define the discount percentage
    DISCOUNT_PERCENTAGE = 0.3

    # Calculate the discounted price of the pants
    pants_discount = PANTS_PRICE * DISCOUNT_PERCENTAGE
    pants_price_discounted = PANTS_PRICE - pants_discount

    # Calculate the discounted price of the socks
    socks_discount = SOCKS_PRICE * DISCOUNT_PERCENTAGE
    socks_price_discounted = SOCKS_PRICE - socks_discount

    # Calculate the total cost of all items after the discount
    total_cost = (pants_price_discounted * 4) + (socks_price_discounted * 2)

    # Display the total cost
    result = total_cost
    return result

print(solution())