def solution():
    """While passing by a store, Miley noticed that a bag that cost $150 last week is now on sale for $135. What percent is the discount?"""
    original_price = 150
    sale_price = 135
    discount_amount = original_price - sale_price
    discount_percent = discount_amount / original_price * 100
    result = discount_percent
    return result

print(solution())