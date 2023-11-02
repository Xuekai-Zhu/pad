def solution():
    
    normal_price = 80
    discount_percent = 45
    discount_amount = normal_price * (discount_percent / 100)
    discounted_price = normal_price - discount_amount
    result = discounted_price
    return result

print(solution())