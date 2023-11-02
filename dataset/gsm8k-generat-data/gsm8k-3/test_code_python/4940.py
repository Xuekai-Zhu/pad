def solution():
    """A shop is offering a discount on pens. If you buy 10 pens at the regular price, you can get the next 10 for half off. A customer came in and bought 20 pens for $30. What's the regular price of one pen in dollars?"""
    # Define the number of pens in each discount tier
    REGULAR_TIER = 10
    DISCOUNT_TIER = 10

    # Define the regular price and the discount price
    REGULAR_PRICE = 1.5
    DISCOUNTED_PRICE = REGULAR_PRICE / 2

    # Define the number of pens purchased and the total cost
    total_pens = 20
    total_cost = 30

    # Calculate the number of pens purchased at regular price and at discount price
    regular_pens = min(total_pens, REGULAR_TIER)
    discount_pens = max(0, total_pens - REGULAR_TIER)

    # Calculate the total cost of the pens purchased at regular price and at discount price
    regular_cost = regular_pens * REGULAR_PRICE
    discount_cost = discount_pens * DISCOUNTED_PRICE

    # Calculate the regular price of one pen
    regular_price = regular_cost / regular_pens

    # Display the regular price of one pen
    result = regular_price
    return result

print(solution())