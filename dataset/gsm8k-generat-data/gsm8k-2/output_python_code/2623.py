def solution():
    """While buying DVDs at the store, Maria received a 25% discount. If the discount she received is $40, how much did she pay in total?"""
    discount_percentage = 0.25
    discount_amount = 40
    original_amount = discount_amount / discount_percentage
    total_amount = original_amount - discount_amount
    result = total_amount
    return result

print(solution())