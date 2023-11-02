def solution():
    """Sam is stocking up on canned tuna. He got 9 cans at the supermarket, and had 5 coupons for 25 cents off a single can per coupon. He paid $20 and got $5.50 in change. How many cents does a can of tuna cost?"""
    num_cans = 9
    coupon_value = 25
    num_coupons = 5
    total_discount = coupon_value * num_coupons
    cost = 2000 - total_discount - 550
    cost_per_can = cost / num_cans
    result = cost_per_can * 100
    return result

print(solution())