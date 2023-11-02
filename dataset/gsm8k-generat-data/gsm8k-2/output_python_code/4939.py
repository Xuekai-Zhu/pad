def solution():
    """A shop is offering a discount on pens. If you buy 10 pens at the regular price, you can get the next 10 for half off. A customer came in and bought 20 pens for $30. What's the regular price of one pen in dollars?"""
    full_price_pens = 10
    half_price_pens = 10
    full_price = 0
    for i in range(1, full_price_pens + 1):
        full_price += 1
    for i in range(1, half_price_pens + 1):
        if i <= half_price_pens/2:
            full_price += 0.5
        else:
            full_price += 1
            
    regular_price = full_price / 20
    result = regular_price
    return result

print(solution())