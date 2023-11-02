def solution():
    original_price = 7.50
    coupon = 2.50
    senior_discount = 0.20  # 20% discount

    # Calculate the price after applying the coupon
    price_after_coupon = original_price - coupon

    # Calculate the price after applying the senior discount
    price_after_discount = price_after_coupon - (price_after_coupon * senior_discount)

    result = price_after_discount
    return result

print(solution())