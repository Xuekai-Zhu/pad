def solution():
    original_price = 150
    sale_price = 135
    discount_amount = original_price - sale_price
    discount_percent = (discount_amount / original_price) * 100
    result = discount_percent
    return result

print(solution())