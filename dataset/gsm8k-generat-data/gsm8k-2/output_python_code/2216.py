def solution():
    """Mrs. Taylor bought two smart televisions that cost $650 each. If the total sales price had a 25% discount, how much did Mrs. Taylor pay for the two televisions?"""
    original_price = 650 * 2
    discount = 0.25
    discounted_price = original_price * (1-discount)
    result = discounted_price
    return result

print(solution())