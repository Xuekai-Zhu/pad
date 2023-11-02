def solution():
    frame_cost = 200
    lens_cost = 500
    insurance_coverage = 0.8 # 80% coverage
    frame_coupon = 50

    # Calculate the discounted frame cost
    discounted_frame_cost = frame_cost - frame_coupon

    # Calculate the cost of the lenses after insurance coverage
    discounted_lens_cost = lens_cost * (1 - insurance_coverage)

    # Calculate the total cost of the glasses
    total_cost = discounted_frame_cost + discounted_lens_cost
    result = total_cost
    return result

print(solution())