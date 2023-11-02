def solution():
    """A customer’s loyalty card at a store gives them rewards of $1 off their next purchase for every $20 they spend. Their last shopping trip, they spent $80. This shopping trip, they spent $43, used their rewards, and applied a coupon that took twice the amount of rewards off the price. How many dollars did the customer pay on this shopping trip?"""
    last_purchase = 80
    rewards_earned = last_purchase // 20
    current_purchase = 43
    rewards_used = rewards_earned
    coupon_used = 2 * rewards_used
    price_before_coupon = current_purchase - rewards_used
    price_after_coupon = price_before_coupon - coupon_used
    result = price_after_coupon
    return result

print(solution())