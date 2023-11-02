def solution():
    """A shop is offering a discount on pens. If you buy 10 pens at the regular price, you can get the next 10 for half off. A customer came in and bought 20 pens for $30. What's the regular price of one pen in dollars?"""
    pens_at_full_price = 10
    pens_at_half_price = 10
    full_price = x
    half_price = full_price / 2
    total_cost = (pens_at_full_price * full_price) + (pens_at_half_price * half_price)
    price_per_pen = total_cost / 20
    result = price_per_pen
    return result

print(solution())