def solution():
    
    original_price = 10
    discount_percent = 10
    discount_amount = (discount_percent/100) * original_price
    discounted_price = original_price - discount_amount
    result = discounted_price
    return result

print(solution())