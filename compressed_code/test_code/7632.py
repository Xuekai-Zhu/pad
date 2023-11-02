def solution():
    
    sale_price = 51
    discount_percent = 75
    original_price = sale_price / (1 - discount_percent/100)
    result = original_price
    return result

print(solution())