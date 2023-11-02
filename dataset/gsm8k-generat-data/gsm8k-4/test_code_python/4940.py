def solution():
    """A shop is offering a discount on pens. If you buy 10 pens at the regular price, you can get the next 10 for half off. A customer came in and bought 20 pens for $30. What's the regular price of one pen in dollars?"""
    # Define the regular price of the pens
    regular_price = None

    # Buy 10 pens at regular price to get the next 10 at half off
    total_price = 10 * regular_price + 10 * (regular_price / 2)

    # Calculate the price per pen
    price_per_pen = total_price / 20

    # Calculate the regular price per pen
    regular_price = price_per_pen * 2

    # return the result
    result = regular_price
    return result

print(solution())