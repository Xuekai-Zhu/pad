def solution():
    
    original_price = 7.5
    coupon = 2.5
    discount = 0.2
    senior_discount_price = (original_price - coupon) * (1 - discount)
    result = senior_discount_price
    return result

print(solution())