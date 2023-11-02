def solution():
    """While buying DVDs at the store, Maria received a 25% discount. If the discount she received is $40, how much did she pay in total?"""
    discount_percent = 25
    discount_amount = 40
    original_price = (100 / (100 - discount_percent)) * discount_amount
    total_price = original_price - discount_amount
    result = total_price
    return result

print(solution())