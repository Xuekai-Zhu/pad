def solution():
    """Anthony is sending out coupons for his pizza parlor through the mail. He wants to send out 700 small coupons and twice as many big coupons. If each small coupon costs 5 cents to mail and each big coupon costs 15 cents, how much does he spend on postage total?"""
    small_coupons = 700
    big_coupons = 2 * small_coupons
    postage_cost_small = 0.05
    postage_cost_big = 0.15
    postage_total = (small_coupons * postage_cost_small) + (big_coupons * postage_cost_big)
    result = postage_total
    return result

print(solution())