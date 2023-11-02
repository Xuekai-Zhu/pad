def solution():
    magazine_cost = 0.85  # Daniel buys a magazine costing $0.85
    pencil_cost = 0.50  # Daniel buys a pencil costing $0.50
    coupon_value = 0.35  # Daniel has a coupon that gives him $0.35 off

    # Calculate the total cost before applying the coupon
    total_cost_before_coupon = magazine_cost + pencil_cost

    # Calculate the total cost after applying the coupon
    total_cost_after_coupon = total_cost_before_coupon - coupon_value
    result = total_cost_after_coupon
    return result

print(solution())