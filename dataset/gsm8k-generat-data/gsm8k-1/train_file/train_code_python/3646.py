def solution():
    """Carla's order at Mcdonald's costs $7.50, but she has a coupon for $2.50. If she gets an additional 20% discount for being a senior citizen, how much does she pay for her order in dollars total?"""
    original_price = 7.50
    coupon_amount = 2.50
    discounted_price = original_price - coupon_amount
    senior_discount = 0.20
    final_price = discounted_price * (1 - senior_discount)
    result = final_price
    return result

print(solution())