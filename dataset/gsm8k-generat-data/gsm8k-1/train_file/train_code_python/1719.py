def solution():
    """Lyra bought a pair of shoes at a 20% discount. If she paid $480, how much was the original price of the pair of shoes?"""
    discounted_price = 480
    discount_percent = 20
    original_price = discounted_price / (1 - (discount_percent / 100))
    result = original_price
    return result

print(solution())