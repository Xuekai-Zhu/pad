def solution():
    original_price = 120
    coupon_discount = 10
    membership_discount = 0.1

    # Calculate the price after applying the coupon discount
    price_after_coupon = original_price - coupon_discount

    # Calculate the price after applying the membership discount
    price_after_membership = price_after_coupon * (1 - membership_discount)

    result = price_after_membership
    return result

print(solution())