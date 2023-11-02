def solution():
    """The price of a laptop is $1000. If you get a 20% discount, how much do you have to pay?"""
    original_price = 1000
    discount_rate = 0.2
    discount_amount = original_price * discount_rate
    sale_price = original_price - discount_amount
    result = sale_price
    return result

print(solution())