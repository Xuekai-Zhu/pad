def solution():
    """A bag has a 5% discount. If it is marked $140, how much will you pay after the discount?"""
    original_price = 140
    discount_percent = 5
    discount_amount = original_price * (discount_percent / 100)
    new_price = original_price - discount_amount
    result = new_price
    return result

print(solution())