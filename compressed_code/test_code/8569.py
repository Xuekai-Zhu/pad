def solution():
    
    total_cost = 25
    coupon = 5
    cost_after_coupon = total_cost - coupon
    total_ounces = 40
    cost_per_ounce = cost_after_coupon / total_ounces
    cost_per_serving = cost_per_ounce * 1 * 100
    result = int(cost_per_serving)
    return result

print(solution())