def solution():
    """Kyle bought last year's best-selling book for $19.50. This is with a 25% discount from the original price. What was the original price of the book?"""
    discount_percent = 25
    discounted_price = 19.5
    original_price = discounted_price / (1 - (discount_percent / 100))
    result = original_price
    return result

print(solution())