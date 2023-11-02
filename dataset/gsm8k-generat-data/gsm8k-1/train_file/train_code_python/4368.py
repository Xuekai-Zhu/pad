def solution():
    """Rose bought a plant with a 10% discount. If the price is $10, how much did Rose pay after the discount?"""
    original_price = 10
    discount_percent = 10
    discount_amount = original_price * (discount_percent / 100)
    discounted_price = original_price - discount_amount
    result = discounted_price
    return result

print(solution())