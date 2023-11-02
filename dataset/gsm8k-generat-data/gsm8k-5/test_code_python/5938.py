def solution():
    original_price = 120  # The original price of the sneakers is $120
    coupon_value = 10  # The coupon is worth $10
    discount_percent = 0.1  # The membership discount is 10%

    # Apply the coupon first
    after_coupon_price = original_price - coupon_value

    # Apply the membership discount on the price after the coupon
    final_price = after_coupon_price * (1 - discount_percent)

    result = final_price
    return result

print(solution())