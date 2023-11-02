def solution():
    original_cost = 7.5
    coupon_value = 2.5
    discounted_cost = original_cost - coupon_value
    senior_discount = discounted_cost * 0.2
    final_cost = discounted_cost - senior_discount
    result = final_cost
    return result

print(solution())