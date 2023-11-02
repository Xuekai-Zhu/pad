def solution():
    
    original_price = 1000
    discount_percent = 20
    discount_amount = original_price * (discount_percent / 100)
    discounted_price = original_price - discount_amount
    result = discounted_price
    return result

print(solution())