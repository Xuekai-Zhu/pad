def solution():
    
    original_price = 90
    discount_percentage = 20
    discount_amount = original_price * (discount_percentage / 100)
    sale_price = original_price - discount_amount
    result = sale_price
    return result

print(solution())