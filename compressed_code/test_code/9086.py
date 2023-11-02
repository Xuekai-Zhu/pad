def solution():
    
    original_price = 80
    discount_percent = 15
    discount_amount = original_price * (discount_percent / 100)
    sale_price = original_price - discount_amount
    result = sale_price
    return result

print(solution())