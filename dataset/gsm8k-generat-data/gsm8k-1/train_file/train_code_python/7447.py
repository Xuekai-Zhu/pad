def solution():
    """A department store displays a 20% discount on all fixtures. What will be the new price of a 25 cm high bedside lamp that was worth $120?"""
    original_price = 120
    discount_percent = 20
    discount_amount = original_price * (discount_percent / 100)
    new_price = original_price - discount_amount
    result = new_price
    return result

print(solution())