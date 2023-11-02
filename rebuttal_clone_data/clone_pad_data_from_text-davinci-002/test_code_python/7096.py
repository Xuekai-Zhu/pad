def solution():
    regular_price = 15
    discount = 0.20
    price_after_discount = regular_price - (regular_price * discount)
    coupon_value = 2
    price_after_coupon = price_after_discount - coupon_value
    total_price = price_after_coupon * 3
    result = total_price
    return result

print(solution())