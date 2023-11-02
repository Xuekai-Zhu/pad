def solution():
    
    original_price = 7.50
    coupon_amount = 2.50
    discounted_price = original_price - coupon_amount
    senior_discount = 0.20
    final_price = discounted_price * (1 - senior_discount)
    result = final_price
    return result

print(solution())