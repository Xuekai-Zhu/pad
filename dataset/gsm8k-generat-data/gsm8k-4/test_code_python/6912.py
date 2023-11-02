def solution():
    """Sam is stocking up on canned tuna. He got 9 cans at the supermarket, and had 5 coupons for 25 cents off a single can per coupon. He paid $20 and got $5.50 in change. How many cents does a can of tuna cost?"""
    # Define the number of cans and the coupon discount
    num_cans = 9
    coupon_discount = 0.25

    # Calculate the total discount from the coupons
    total_discount = 5 * coupon_discount

    # Calculate the total cost of the cans before the discount
    total_cost_before_discount = num_cans * 1.0

    # Calculate the total cost of the cans after the discount
    total_cost_after_discount = total_cost_before_discount - total_discount

    # Calculate the actual amount paid by Sam
    actual_paid = 20 - 5.5

    # Calculate the cost per can
    cost_per_can = actual_paid / total_cost_after_discount

    # Convert the cost per can to cents
    cost_per_can_cents = cost_per_can * 100

    result = round(cost_per_can_cents)
    return result

print(solution())