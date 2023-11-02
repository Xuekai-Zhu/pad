def solution():
    
    original_price = 125
    sale_price = original_price * 0.8
    coupon_price = sale_price - 10
    remaining_price = coupon_price * 0.9
    saved_price = original_price - remaining_price
    result = saved_price
    return result

print(solution())