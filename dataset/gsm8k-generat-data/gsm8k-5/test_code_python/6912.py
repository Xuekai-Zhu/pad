def solution():
    num_cans = 9  # Sam got 9 cans of tuna
    discount_per_coupon = 0.25  # Each coupon gives a discount of 25 cents
    num_coupons = 5  # Sam used 5 coupons

    # Calculate the total discount from the coupons
    total_discount = discount_per_coupon * num_coupons

    # Calculate the total cost of the tuna cans
    total_cost = 20 - 5.5 + total_discount

    # Calculate the cost per can in cents
    cost_per_can_cents = (total_cost * 100) / num_cans
    result = cost_per_can_cents
    return result

print(solution())