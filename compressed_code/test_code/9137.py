def solution():
    
    regular_price = 15
    discount_percent = 40
    discount_amount = regular_price * (discount_percent / 100)
    sale_price = regular_price - discount_amount
    result = sale_price
    return result

print(solution())