def solution():
    """Davos bought 2 shirts from the mall that cost $30 each. If he bought them with a 40% discount, how much did Davos pay for the 2 shirts?"""
    original_price = 30
    discount_percent = 40
    discount_amount = original_price * (discount_percent / 100)
    sale_price = original_price - discount_amount
    total_price = 2 * sale_price
    result = total_price
    return result

print(solution())