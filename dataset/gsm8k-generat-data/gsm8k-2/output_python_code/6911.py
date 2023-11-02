def solution():
    """Sam is stocking up on canned tuna. He got 9 cans at the supermarket, and had 5 coupons for 25 cents off a single can per coupon. He paid $20 and got $5.50 in change. How many cents does a can of tuna cost?"""
    num_cans = 9
    coupon_discount = 0.25
    num_coupons = 5
    coupon_savings = coupon_discount * num_coupons
    total_cost = 20
    change = 5.5
    cost_per_can = (total_cost - change - coupon_savings) / num_cans
    cost_in_cents = cost_per_can * 100
    result = cost_in_cents
    return result

print(solution())