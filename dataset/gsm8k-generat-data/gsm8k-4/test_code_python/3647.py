def solution():
    """Carla's order at Mcdonald's costs $7.50, but she has a coupon for $2.50. If she gets an additional 20% discount for being a senior citizen, how much does she pay for her order in dollars total?"""
    # Define the initial cost and the coupon value
    INITIAL_COST = 7.50
    COUPON_VALUE = 2.50

    # Calculate the subtotal after the coupon
    subtotal = INITIAL_COST - COUPON_VALUE

    # Calculate the discount for being a senior citizen
    discount = subtotal * 0.20

    # Calculate the total cost after the discount
    total_cost = subtotal - discount

    result = total_cost
    return result

print(solution())