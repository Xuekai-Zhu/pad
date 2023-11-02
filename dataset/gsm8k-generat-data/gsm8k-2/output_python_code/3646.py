def solution():
    """Carla's order at Mcdonald's costs $7.50, but she has a coupon for $2.50. If she gets an additional 20% discount for being a senior citizen, how much does she pay for her order in dollars total?"""
    original_price = 7.5
    coupon = 2.5
    discount = 0.2
    senior_discount_price = (original_price - coupon) * (1 - discount)
    result = senior_discount_price
    return result

print(solution())