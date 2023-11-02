def solution():
    # Define the given values
    frame_cost = 200
    lens_cost = 500
    insurance_coverage = 0.8
    coupon_discount = 50

    # Calculate the discounted frame cost
    discounted_frame_cost = frame_cost - coupon_discount

    # Calculate the cost of the lenses after insurance coverage
    covered_lens_cost = lens_cost * insurance_coverage

    # Calculate the total cost of everything
    total_cost = discounted_frame_cost + covered_lens_cost
    result = total_cost
    return result

print(solution())