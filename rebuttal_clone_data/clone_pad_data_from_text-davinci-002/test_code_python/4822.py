def solution():
    frame_cost = 200
    lens_cost = 500
    insurance_coverage = 0.8
    coupon_discount = 50
    net_lens_cost = lens_cost * (1 - insurance_coverage)
    net_frame_cost = frame_cost - coupon_discount
    total_cost = net_frame_cost + net_lens_cost
    result = total_cost
    return result

print(solution())