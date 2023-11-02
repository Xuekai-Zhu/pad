def solution():
    original_price = 120
    discount_percent = 20
    discount_amount = original_price * (discount_percent/100)
    new_price = original_price - discount_amount

    result = new_price
    return result

print(solution())