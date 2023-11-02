def solution():
    # Calculate the total cost of the 9 cans of tuna
    total_cost = 20 - 5.5  # Sam paid $20 and got $5.50 in change
    # Calculate the value of the coupons used
    coupon_value = 5 * 0.25  # Sam had 5 coupons worth 25 cents each
    # Subtract the value of the coupons from the total cost to find the cost of the tuna without coupons
    cost_without_coupons = total_cost - coupon_value
    # Divide the cost without coupons by the number of cans to find the cost per can in cents
    cost_per_can = (cost_without_coupons * 100) / 9
    result = cost_per_can
    return result

print(solution())