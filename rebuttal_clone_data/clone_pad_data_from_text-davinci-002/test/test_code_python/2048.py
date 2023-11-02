def solution():
    cost_before_coupon = 7.50
    coupon_value = 2.50
    senior_discount = 20
    cost_after_coupon = cost_before_coupon - coupon_value
    senior_discount_amount = cost_after_coupon * (senior_discount / 100)
    total_cost = cost_after_coupon - senior_discount_amount
    result = total_cost
    return result

print(solution())