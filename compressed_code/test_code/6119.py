def solution():
    
    original_price = 6.00
    discount_percent = 75
    discount_amount = original_price * (discount_percent / 100)
    price_after_discount = original_price - discount_amount
    total_price = price_after_discount * 2
    result = total_price
    return result

print(solution())