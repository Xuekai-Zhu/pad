def solution():
    
    original_price = 200
    sale_price = original_price * 0.75
    tax_rate = 0.1
    total_price = sale_price * (1 + tax_rate)
    result = total_price
    return result

print(solution())