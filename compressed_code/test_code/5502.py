def solution():
    
    original_price = 350
    sale_price = 140
    discount = (original_price - sale_price) / original_price
    percent_off = discount * 100
    result = percent_off
    return result

print(solution())