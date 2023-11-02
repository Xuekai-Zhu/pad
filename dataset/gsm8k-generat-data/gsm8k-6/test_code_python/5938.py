def solution():
    # Calculate the price of the sneakers after the coupon is applied
    price_after_coupon = 120 - 10  # the man has a $10 off coupon

    # Calculate the price of the sneakers after the membership discount is applied
    price_after_membership = price_after_coupon * 0.9  # the man receives a 10% off membership discount

    result = price_after_membership
    return result

print(solution())