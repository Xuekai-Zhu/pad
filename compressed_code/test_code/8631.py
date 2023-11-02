def solution():
    
    sale_price = 450
    discount_percent = 10
    original_price = sale_price / ((100-discount_percent) / 100)
    result = original_price
    return result

print(solution())