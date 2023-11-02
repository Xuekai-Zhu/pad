def solution():
    original_price = 120
    coupon_discount = 10
    membership_discount = 0.1

    # Apply coupon discount first
    price_after_coupon = original_price - coupon_discount

    # Apply membership discount next
    price_after_membership_discount = price_after_coupon * (1 - membership_discount)

    result = price_after_membership_discount
    return result

print(solution())