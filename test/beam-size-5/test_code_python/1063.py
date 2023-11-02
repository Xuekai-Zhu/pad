def solution():
    small_coupons = 700  # Anthony wants to send out 700 small coupons
    big_coupons = 2 * small_coupons  # Anthony wants to send out twice as many big coupons as small coupons
    small_coupon_cost = 5  # Each small coupon costs 5 cents
    big_coupon_cost = 15  # Each big coupon costs 15 cents

    # Calculate the total cost of postage
    total_cost = (small_coupons * small_coupon_cost) + (big_coupons * big_coupon_cost)
    result = total_cost
    return result

print(solution())