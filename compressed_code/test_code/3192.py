def solution():
    
    discounted_price = 500
    units = 18
    discount_threshold = 15
    discount_percent = 20/100
    if units > discount_threshold:
        original_price = discounted_price / (1 - discount_percent)
    else:
        original_price = discounted_price
    
    result = original_price
    return result

print(solution())