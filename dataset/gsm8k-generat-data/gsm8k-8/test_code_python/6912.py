def solution():
    # Define the known values
    num_cans = 9
    coupon_discount = 0.25
    num_coupons = 5
    total_paid = 2000 # in cents
    total_change = 550 # in cents

    # Calculate the total cost before coupons
    cost_before_coupons = total_paid + total_change
    cost_before_coupons -= num_coupons * coupon_discount * 100

    # Calculate the cost per can
    cost_per_can = cost_before_coupons / num_cans
    result = cost_per_can
    return result

print(solution())