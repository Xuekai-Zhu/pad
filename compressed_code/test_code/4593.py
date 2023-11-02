def solution():
    
    sneaker_price = 120
    coupon_value = 10
    discount_percentage = 10/100
    discounted_price = sneaker_price - coupon_value
    final_price = discounted_price - (discounted_price * discount_percentage)
    result = final_price
    return result

print(solution())